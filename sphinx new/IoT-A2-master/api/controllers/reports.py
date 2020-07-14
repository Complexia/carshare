from api import db
from models import Car, Report
from flask import jsonify

# performs request response for routes pertaining to the Report resource
class ReportController:
# report controller must be able to obtain cars to construct a report object
    def __getCar(self, id):
        carTuple = db.getObjectById('cars', id)[0]
        if not carTuple:
            return None
        return Car(carTuple[0], carTuple[1], carTuple[2], carTuple[3], carTuple[4], carTuple[5], carTuple[6], carTuple[7], carTuple[8])

    def getReport(self, id):
        # locate a report in the database
        reportTuple = db.getObjectById('reports', id)[0]
        # use data to create a report object then jsonify it's dict
        return jsonify(Report(reportTuple[0], self.__getCar(reportTuple[1]), reportTuple[2], reportTuple[3]).asDict())

    def getReports(self, params=None):
        reports = []

        if not params:
            reportTuples = db.getAllObjects('reports')
        else:
            for param in params:
                if param not in Report.attributesAsList():
                    return jsonify({'reports': []})
            reportTuples = db.getObjectsByFilter('reports', list(params.keys()), list(params.values()))

        # contsruct the fetched reports as objects
        for i in range(len(reportTuples)):
            reports.append(Report(reportTuples[i][0], self.__getCar(reportTuples[i][1]), reportTuples[i][2], reportTuples[i][3]))

        # jsonify each report object's dict
        return jsonify(reports=[report.asDict() for report in reports])

    def createReport(self, params):
        # construct a report object from the gathered data
        report = Report(params[0], self.__getCar(params[1]), params[2], params[3])
        # update the database with the new report and respond with a confirmation of insertion
        db.insertObject('reports', Report.attributesAsList(), report.asTuple())
        return jsonify({'report': report.asDict()}), 201

    def updateReport(self, id, fieldsToUpdate, params):
        # update the report with the specified id, indicating which fields to update and what to update them to
        db.updateObject('reports', id, fieldsToUpdate, params)
        # retrieve the newly updated report and create an object from it's data
        reportTuple = db.getObjectById('reports', id)[0]
        report = Report(reportTuple[0], self.__getCar(reportTuple[1]), reportTuple[2], reportTuple[3])
        # jsonify the report to confirm the update
        return jsonify({'report': report.asDict()})

    def deleteReport(self, id):
        db.deleteObject('reports', id)
        return jsonify({'result': True})

# create a single instance of a ReportController to be exported
reportsController = ReportController()