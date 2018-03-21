#Methods needed for Bugbin from Taiga Comm
# Get Issue
# Create Issue
# Comment on issue
# Edit Issue
# Change status for issue



#Example for Get Issue:
import taiga_comm

comm=taiga_comm.TaigaCommunicator()
comm.AuthUser("Username","password")
comm.GetIssue("974279")


#Example for Create Issue:
import taiga_comm

comm=taiga_comm.TaigaCommunicator()
comm.AuthUser("Username","password")
comm.CreateIssue(projectid=92046, type="Bug" 
,subject="subject", description="Issue Description" 
, priority = "Normal", severity="Normal" 
, status="Level 1" , tags=["Bot","bugbin"])

#Example for Comment on Issue:
import taiga_comm

comm=taiga_comm.TaigaCommunicator()
comm.AuthUser("Username","password")
comm.EditIssue(issueId='974279', comment="This Issue has been released")

#Example for Edit Issue:
import taiga_comm

comm=taiga_comm.TaigaCommunicator()
comm.AuthUser("Username","password")
comm.EditIssue(issueId='974279', subject="Moviepass: Production issue: 500 errors: Clean up Access tokens and check for multiple DB calls", description="description" , comment="This Issue has been released")

#Example for change Status of Issue
import taiga_comm

comm=taiga_comm.TaigaCommunicator()
comm.AuthUser("Username","password")
comm.EditIssue(issueId="974279", status=str(comm.getIssueStatusid("Ready for Prod"))

