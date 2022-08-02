import logging,sys
from flask import Flask
from Petrol_price.logger import logging
from Petrol_price.exception import ForcastException


app=Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    try:
        raise Exception("djhfgdsfgdfkdsfkjds")
    except Exception as e:
        forcast=ForcastException(e,sys)
        logging.info(forcast.error_message)
        logging.info("we are pasting logginf")
    return "starting mahine learning PROJECTING and completed ci/cd pipeline"



if __name__=="__main__":
    app.run(debug=True)
