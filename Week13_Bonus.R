# Q1
df = read.table("C:/Users/Kile/Desktop/Code_Temp/job_info_file.txt", sep = "~", header = T, stringsAsFactors = F)
Date = df$Date
Date = as.factor(substr(Date,nchar(Date)-3,nchar(Date)))
df$Date = Date
dt = table(df$Date,df$Specialty)

# plot1
par(mar=c(5.1, 9 ,4.1 ,1))
x_range = c(min(prop.table(dt["2013",])),max(prop.table(dt["2013",]))+0.05)
barplot(sort(sort(prop.table(dt["2013",]),decreasing = T)[1:5]),border=NA,xlim=x_range,horiz = TRUE, col = "springgreen3",
        main = "Hot Specialties of 2013", cex.names=0.8,las = 1, xlab = "Percentage")

# plot2
par(mar=c(5.1, 9 ,4.1 ,1))
x_range = c(min(prop.table(dt["2014",])),max(prop.table(dt["2014",]))+0.05)
barplot(sort(sort(prop.table(dt["2014",]),decreasing = T)[1:5]),border=NA,xlim=x_range,horiz = TRUE, col = "springgreen3",
        main = "Hot Specialties of 2014", cex.names=0.8,las = 1, xlab = "Percentage")

# plot3
par(mar=c(5.1, 9 ,4.1 ,1))
x_range = c(min(prop.table(dt["2015",])),max(prop.table(dt["2015",]))+0.05)
barplot(sort(sort(prop.table(dt["2015",]),decreasing = T)[1:5]),border=NA,xlim=x_range,horiz = TRUE, col = "springgreen3",
        main = "Hot Specialties of 2015", cex.names=0.8,las = 1, xlab = "Percentage")

# Q2
df = readLines("C:/Users/Kile/Desktop/Code_Temp/Salary_info_file.txt")
for(i in 1:length(df)){
    if(grepl("\\(Telecommute\\)",df[i])==TRUE){
        df[i] = gsub("\\(Telecommute\\)",df[i-1],df[i])  
        
    }
}
df = df[substr(df,1,1)!="-"]
df = df[substr(df,nchar(df)-3,nchar(df))!="None"]
df = df[grepl(";", df)==TRUE]
df = df[grepl("\\.", df)==FALSE]
for(i in 1:length(df)){
    if(grepl("\\(",df[i])==TRUE){
        df[i] = gsub("\\(","",df[i]) 
    }
}
df = df[nchar(substr(df,regexpr(',', df),length(df)))==4]
df = gsub(",","",df)
dollar_sign = substr(df,regexpr(';', df)+1,regexpr(';', df)+1)

loc = c()
sal = c()
for(i in 1:length(dollar_sign)){
    loc[i] = substr(df[i],1,regexpr(';', df[i])-1)
    if(dollar_sign[i]=="$"){
        sal[i] = as.numeric(substr(df[i],regexpr(';', df[i])+2,nchar(df[i])))
    }else if(dollar_sign[i]=="¢G"){
        sal[i] = round(1.516*as.numeric(substr(df[i],regexpr(';', df[i])+2,nchar(df[i]))),0)
    }else{
        sal[i] = as.numeric(substr(df[i],regexpr(';', df[i])+1,nchar(df[i])))
    }
}
old.par <- par(mar = c(0, 0, 0, 0))
par(old.par)
df = data.frame(loc, sal)
df$loc = factor(df$loc)
boxplot(df$sal~df$loc, cex.axis=0.5)
