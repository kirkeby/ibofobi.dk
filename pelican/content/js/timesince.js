/* =================================================================================================
* Time Since
* January 16, 2004
*
* Time Since creates a string which friendly tells you the time since the original date
* Based on the original time_since() function by Natalie Downe - http://blog.natbat.co.uk/archive/2003/Jun/14/time_since
*
* Copyright (c) 2004 Mark Wubben - http://neo.dzygn.com/
*
* Usage: date.toTimeSinceString(number nLimit, string sBetween, string sLastBetween)
* nLimit: limit the shown time units (year, month etc). default = 2
* sBetween: string between two time units. default = ", "
* sLastBetween: string between the second-last and last time unit. default = " and "
==================================================================================================*/
Date.prototype.toTimeSinceString = function(nLimit, sBetween, sLastBetween){
	if(!nLimit){ nLimit = 2; }
	if(!sBetween){ sBetween = ", "; }
	if(!sLastBetween){ sLastBetween = " and "; }
	if(!Date.prototype.toTimeSinceString._collStructs){
		Date.prototype.toTimeSinceString._collStructs = new Array(
			{seconds: 60 * 60 * 24 * 365, name: "year"},
			{seconds: 60 * 60 * 24 * 30, name: "month"},
			{seconds: 60 * 60 * 24 * 7, name: "week"},
			{seconds: 60 * 60 * 24, name: "day"},
			{seconds: 60 * 60, name: "hour"},
			{seconds: 60, name: "minute"}
		);
	}

	var collStructs = Date.prototype.toTimeSinceString._collStructs;
	var nSecondsRemain = ((new Date).valueOf() - this.valueOf()) / 1000;
	var sReturn = "";
	var nCount = 0;
	var nFloored;

	for(var i = 0; i < collStructs.length && nCount < nLimit; i++){
		nFloored = Math.floor(nSecondsRemain / collStructs[i].seconds);
		if(nFloored > 0){
			if(sReturn.length > 0){
				if(nCount == nLimit - 1 || i == collStructs.length - 1){
					sReturn += sLastBetween;
				} else if(nCount < nLimit && i < collStructs.length){
					sReturn += sBetween;
				}
			}
			sReturn += nFloored + " " + collStructs[i].name;
			if(nFloored > 1){
				sReturn += "s";
			}
			nSecondsRemain -= nFloored * collStructs[i].seconds;
			nCount++;
		}
	}

	return sReturn;
}