class Report:
    def get_result(self, terminalreporter):
        passmd, fail, skip = [], [], []
        for status, reports in terminalreporter.stats.items():

            match status:
                case "passed":
                    for report in reports:
                        nodeid = report.nodeid
                        reason = report.longreprtext
                        passmd.append({nodeid: reason})
                case "failed":
                    for report in reports:
                        nodeid = report.nodeid
                        reason = report.longreprtext
                        fail.append({nodeid: reason})
                case "skipped":
                    for report in reports:
                        nodeid = report.nodeid
                        reason = report.longreprtext
                        skip.append({nodeid: reason})
        return passmd, fail, skip
