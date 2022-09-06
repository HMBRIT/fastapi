from fastapi import APIRouter, Response, status, HTTPException
from v1.Analysis.hmbrAnalysis.zepto_overall_analysis import zeptoOverAll
from v1.Analysis.hmbrAnalysis.sales_report_analysis_hmbr import salesReportMain
from v1.Analysis.hmbrAnalysis.transport_analysis_hmbr import transportAnalysis
import shutil

router = APIRouter()

@router.get("/api/v1/hmbr/transport", tags=["transport"])
async def transport ():
    x = transportAnalysis ()
    return {"data": x}


@router.get("/api/v1/hmbr/salesreport", tags=["salesreport"])
async def salesreport ():
    salesReportMain()
    return {"data": "success"}

@router.post("/api/v1/hmbr/zeptooverall", tags=["zepto overall reports"] , status_code=status.HTTP_200_OK)
async def zeptoOverallReport ():
    zeptoOverAll()
    shutil.move("F:/11FastApiRouting/app/index.html", "F:/11FastApiRouting/app/v1/Analysis/hmbrAnalysis/index.html")
    shutil.move("F:/11FastApiRouting/app/ZeptoOverall.xlsx", "F:/11FastApiRouting/app/v1/Analysis/hmbrAnalysis/index.html")
    return {"data": "success"}



