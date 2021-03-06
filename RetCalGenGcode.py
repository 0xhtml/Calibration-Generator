from decimal import Decimal


def genGcode(name, srd, ird, srs, irs, tsh, tih, fs, fsi, lh, ts, lt, nt, dx, dy, ps, nd, fd, em, tb, sgcode):
    file = open(name, 'w')

    file.write(f";Calibration Generator 1.3.3\n")
    file.write(f";\n")
    file.write(f";\n")
    file.write(f";Retraction Distance from the top looking down\n")
    file.write(f";\n")
    file.write(f";       {round(Decimal(srd+ird*11),2)}    {round(Decimal(srd+ird*10),2)}    {round(Decimal(srd+ird*9),2)}    {round(Decimal(srd+ird*8),2)}\n")
    file.write(f";		|		|		|		|\n")
    file.write(f";\n")
    file.write(f";{round(Decimal(srd+ird*12),2)}-                               -{round(Decimal(srd+ird*7),2)}\n")
    file.write(f";\n")
    file.write(f";\n")
    file.write(f";{round(Decimal(srd+ird*13),2)}-                               -{round(Decimal(srd+ird*6),2)}\n")
    file.write(f";\n")
    file.write(f";\n")
    file.write(f";{round(Decimal(srd+ird*14),2)}-                               -{round(Decimal(srd+ird*5),2)}\n")
    file.write(f";\n")
    file.write(f";\n")
    file.write(f";{round(Decimal(srd+ird*15),2)}-                               -{round(Decimal(srd+ird*4),2)}\n")
    file.write(f";\n")
    file.write(f";		|		|		|		|\n")
    file.write(f";       {round(Decimal(srd+ird*0),2)}    {round(Decimal(srd+ird*1),2)}    {round(Decimal(srd+ird*2),2)}    {round(Decimal(srd+ird*3),2)}\n")
    file.write(f";\n")
    file.write(f";\n")

    file.write(f";Variables by Height\n")
    file.write(f";\n")
    file.write(f";Height         Retraction  Nozzle      Fan\n")
    file.write(f";               Speed       Temp        Speed\n")
    file.write(f";\n")

    cnt = int(nt-1)

    for loopx in range(int(nt)):
        file.write(f";{int(lt)} layers      {round(Decimal(srs+irs*cnt),2)}      {round(Decimal(tsh+tih*cnt),2)}      {round(Decimal(fs+fsi*cnt),2)}\n")
        cnt = cnt-1

    file.write(f";\n")
    file.write(f";\n")
    file.write(f";All inputs\n")
    file.write(f";\n")
    file.write(f";Dimension X 					{int(dx)}\n")
    file.write(f";Dimension Y 					{int(dy)}\n")
    file.write(f";Starting Retraction Distance	{srd}\n")
    file.write(f";Increment Retraction 			{ird}\n")
    file.write(f";Start Retraction Speed 		{srs}\n")
    file.write(f";Retraction Speed Increment 	{irs}\n")
    file.write(f";Print Speed 					{ps}\n")
    file.write(f";Starting Temp 					{int(tsh)}\n")
    file.write(f";Increment Temp 				{int(tih)}\n")
    file.write(f";Bed Temp 						{int(tb)}\n")
    file.write(f";Fan Speed 						{int(fs)}\n")
    file.write(f";Fan Speed Increment 			{int(fsi)}\n")
    file.write(f";Nozzle Diameter 				{nd}\n")
    file.write(f";Layer Height 					{lh}\n")
    file.write(f";Filament Diameter 				{fd}\n")
    file.write(f";Extrusion Multiplier 			{em}\n")
    file.write(f";Layers Per Test                {lt}\n")
    file.write(f";Number of Tests                {nt}\n")
    file.write(f";\n")
    file.write(f";\n")

    def eValue(extrusionLength):
        area = (nd - lh) * lh + 3.14159 * (lh/2)**2
        eValueresult = (area * extrusionLength * 4)/(3.14159 * fd**2/em)
        return eValueresult

    file.write(f";Start Gcode\n")
    file.write(f"M140 S{int(tb)}\n")
    file.write(f"M105\n")
    file.write(f"M190 S{int(tb)}\n")
    file.write(f"M104 S{int(tsh)}\n")
    file.write(f"M105\n")
    file.write(f"M109 S{int(tsh)}\n")
    file.write(f"M82\n")
    file.write(f"G28\n")
    file.write(f"G92 E0\n")
    file.write(f"G1 F200 E1\n")
    file.write(f"G92 E0\n")

    file.write(f"{sgcode}\n")

    file.write(f";\n")
    file.write(f";\n")

    xpos = dx/2-30
    ypos = dy/2-30
    zpos = lh
    epos = 0

    file.write(f";Start Movement\n")
    file.write(f";\n")
    file.write(f"G1 Z2\n")
    file.write(f"G1 F{int(ts)*60} X{xpos} Y{ypos} Z{zpos}\n")
    file.write(f";\n")
    eValueresult = eValue(60)

    evalueincrease = eValueresult*1.25
    eValueresult = evalueincrease

    remx = xpos
    remy = ypos

    file.write(f";Layer 1\n")

    for loopx in range(30):
        file.write(f"G1 F{int(ps*60/2)} X{xpos+60} Y{ypos} E{round(Decimal(eValueresult),5)}\n")
        xpos = xpos + 60
        eValueresult = eValueresult + evalueincrease
        file.write(f"G0 F{int(ts)*60} X{xpos} Y{ypos+1}\n")
        ypos = ypos + 1
        file.write(f"G1 F{int(ps*60/2)} X{xpos-60} Y{ypos} E{round(Decimal(eValueresult),5)}\n")
        xpos = xpos - 60
        eValueresult = eValueresult + evalueincrease
        file.write(f"G0 F{int(ts)*60} X{xpos} Y{ypos+1}\n")
        ypos = ypos + 1

    file.write(f"G0 F{int(ts)*60} X{xpos} Y{ypos} Z{round(Decimal(lh*3),2)}\n")
    file.write(f"G0 F{int(ts)*60} X{remx} Y{remy} Z{lh+lh}\n")
    xpos = remx
    ypos = remy

    file.write(f";Layer 2\n")

    for loopx in range(30):
        file.write(f"G1 F{int(ps*60/2)} X{xpos} Y{ypos+60} E{round(Decimal(eValueresult),5)}\n")
        ypos = ypos + 60
        eValueresult = eValueresult + evalueincrease
        file.write(f"G0 F{int(ts)*60} X{xpos+1} Y{ypos}\n")
        xpos = xpos + 1
        file.write(f"G1 F{int(ps*60/2)} X{xpos} Y{ypos-60} E{round(Decimal(eValueresult),5)}\n")
        ypos = ypos - 60
        eValueresult = eValueresult + evalueincrease
        file.write(f"G0 F{int(ts)*60} X{xpos+1} Y{ypos}\n")
        xpos = xpos + 1

    file.write(f"G0 F{int(ts)*60} X{remx+5} Y{remy+5} Z{round(Decimal(lh*3),2)}\n")

    file.write(f"M83\n")
    file.write(f"G91\n")

    eValueresult = eValue(10)
    corenermarker = eValue(1)

    loopbigcount = 0
    loopsmallcount = 0

    layer = 3

    cnt = int(nt)
    lt = lt - 1

    for loopbig in range(int(cnt)):
        file.write(f"M106 S{(round(Decimal((fs+fsi*loopbigcount)) * 255 / 100,0))  }\n")
        file.write(f"M104 S{round(Decimal(tsh+tih*loopbigcount),0)}\n")

        file.write(f";Layer {layer}\n")

        file.write(f"G1 F{int(ps*60)} X-2 E{round(Decimal(corenermarker),5)}\n")
        file.write(f"G1 F{int(ps*60)} Y-2 E{round(Decimal(corenermarker),5)}\n")
        file.write(f"G1 F{int(ps*60)} X2 E{round(Decimal(corenermarker),5)}\n")
        file.write(f"G1 F{int(ps*60)} Y2 E{round(Decimal(corenermarker),5)}\n")

        file.write(f"G1 F{int(ps*60)} X10 E{round(Decimal(eValueresult),5)}\n")
        file.write(f"G1 E{round(Decimal(srd+ird*0),2) * -1} F{round(Decimal((srs+irs*loopbigcount) * 60),2)}\n")
        file.write(f"G0 F{int(ts)*60} Y-10\n")
        file.write(f"G0 F{int(ts)*60} Y10\n")
        file.write(f"G1 E{round(Decimal(srd+ird*0),2)} F{round(Decimal((srs+irs*loopbigcount) * 60),2)}\n")
        file.write(f"G1 F{int(ps*60)} X10 E{round(Decimal(eValueresult),5)}\n")
        file.write(f"G1 E{round(Decimal(srd+ird*1),2) * -1} F{round(Decimal((srs+irs*loopbigcount) * 60),2)}\n")
        file.write(f"G0 F{int(ts)*60} Y-10\n")
        file.write(f"G0 F{int(ts)*60} Y10\n")
        file.write(f"G1 E{round(Decimal(srd+ird*1),2)} F{round(Decimal((srs+irs*loopbigcount) * 60),2)}\n")
        file.write(f"G1 F{int(ps*60)} X10 E{round(Decimal(eValueresult),5)}\n")
        file.write(f"G1 E{round(Decimal(srd+ird*2),2) * -1} F{round(Decimal((srs+irs*loopbigcount) * 60),2)}\n")
        file.write(f"G0 F{int(ts)*60} Y-10\n")
        file.write(f"G0 F{int(ts)*60} Y10\n")
        file.write(f"G1 E{round(Decimal(srd+ird*2),2)} F{round(Decimal((srs+irs*loopbigcount) * 60),2)}\n")
        file.write(f"G1 F{int(ps*60)} X10 E{round(Decimal(eValueresult),5)}\n")
        file.write(f"G1 E{round(Decimal(srd+ird*3),2) * -1} F{round(Decimal((srs+irs*loopbigcount) * 60),2)}\n")
        file.write(f"G0 F{int(ts)*60} Y-10\n")
        file.write(f"G0 F{int(ts)*60} Y10\n")
        file.write(f"G1 E{round(Decimal(srd+ird*3),2)} F{round(Decimal((srs+irs*loopbigcount) * 60),2)}\n")
        file.write(f"G1 F{int(ps*60)} X10 E{round(Decimal(eValueresult),5)}\n")

        file.write(f"G1 F{int(ps*60)} X1 E{round(Decimal(corenermarker),5)}\n")
        file.write(f"G1 F{int(ps*60)} Y-1 E{round(Decimal(corenermarker),5)}\n")
        file.write(f"G1 F{int(ps*60)} X-1 E{round(Decimal(corenermarker),5)}\n")
        file.write(f"G1 F{int(ps*60)} Y1 E{round(Decimal(corenermarker),5)}\n")

        file.write(f"G1 F{int(ps*60)} Y10 E{round(Decimal(eValueresult),5)}\n")
        file.write(f"G1 E{round(Decimal(srd+ird*4),2) * -1} F{round(Decimal((srs+irs*loopbigcount) * 60),2)}\n")
        file.write(f"G0 F{int(ts)*60} X10\n")
        file.write(f"G0 F{int(ts)*60} X-10\n")
        file.write(f"G1 E{round(Decimal(srd+ird*4),2)} F{round(Decimal((srs+irs*loopbigcount) * 60),2)}\n")
        file.write(f"G1 F{int(ps*60)} Y10 E{round(Decimal(eValueresult),5)}\n")
        file.write(f"G1 E{round(Decimal(srd+ird*5),2) * -1} F{round(Decimal((srs+irs*loopbigcount) * 60),2)}\n")
        file.write(f"G0 F{int(ts)*60} X10\n")
        file.write(f"G0 F{int(ts)*60} X-10\n")
        file.write(f"G1 E{round(Decimal(srd+ird*5),2)} F{round(Decimal((srs+irs*loopbigcount) * 60),2)}\n")
        file.write(f"G1 F{int(ps*60)} Y10 E{round(Decimal(eValueresult),5)}\n")
        file.write(f"G1 E{round(Decimal(srd+ird*6),2) * -1} F{round(Decimal((srs+irs*loopbigcount) * 60),2)}\n")
        file.write(f"G0 F{int(ts)*60} X10\n")
        file.write(f"G0 F{int(ts)*60} X-10\n")
        file.write(f"G1 E{round(Decimal(srd+ird*6),2)} F{round(Decimal((srs+irs*loopbigcount) * 60),2)}\n")
        file.write(f"G1 F{int(ps*60)} Y10 E{round(Decimal(eValueresult),5)}\n")
        file.write(f"G1 E{round(Decimal(srd+ird*7),2) * -1} F{round(Decimal((srs+irs*loopbigcount) * 60),2)}\n")
        file.write(f"G0 F{int(ts)*60} X10\n")
        file.write(f"G0 F{int(ts)*60} X-10\n")
        file.write(f"G1 E{round(Decimal(srd+ird*7),2)} F{round(Decimal((srs+irs*loopbigcount) * 60),2)}\n")
        file.write(f"G1 F{int(ps*60)} Y10 E{round(Decimal(eValueresult),5)}\n")

        file.write(f"G1 F{int(ps*60)} X1 E{round(Decimal(corenermarker),5)}\n")
        file.write(f"G1 F{int(ps*60)} Y1 E{round(Decimal(corenermarker),5)}\n")
        file.write(f"G1 F{int(ps*60)} X-1 E{round(Decimal(corenermarker),5)}\n")
        file.write(f"G1 F{int(ps*60)} Y-1 E{round(Decimal(corenermarker),5)}\n")

        file.write(f"G1 F{int(ps*60)} X-10 E{round(Decimal(eValueresult),5)}\n")
        file.write(f"G1 E{round(Decimal(srd+ird*8),2) * -1} F{round(Decimal((srs+irs*loopbigcount) * 60),2)}\n")
        file.write(f"G0 F{int(ts)*60} Y10\n")
        file.write(f"G0 F{int(ts)*60} Y-10\n")
        file.write(f"G1 E{round(Decimal(srd+ird*8),2)} F{round(Decimal((srs+irs*loopbigcount) * 60),2)}\n")
        file.write(f"G1 F{int(ps*60)} X-10 E{round(Decimal(eValueresult),5)}\n")
        file.write(f"G1 E{round(Decimal(srd+ird*9),2) * -1} F{round(Decimal((srs+irs*loopbigcount) * 60),2)}\n")
        file.write(f"G0 F{int(ts)*60} Y10\n")
        file.write(f"G0 F{int(ts)*60} Y-10\n")
        file.write(f"G1 E{round(Decimal(srd+ird*9),2)} F{round(Decimal((srs+irs*loopbigcount) * 60),2)}\n")
        file.write(f"G1 F{int(ps*60)} X-10 E{round(Decimal(eValueresult),5)}\n")
        file.write(f"G1 E{round(Decimal(srd+ird*10),2) * -1} F{round(Decimal((srs+irs*loopbigcount) * 60),2)}\n")
        file.write(f"G0 F{int(ts)*60} Y10\n")
        file.write(f"G0 F{int(ts)*60} Y-10\n")
        file.write(f"G1 E{round(Decimal(srd+ird*10),2)} F{round(Decimal((srs+irs*loopbigcount) * 60),2)}\n")
        file.write(f"G1 F{int(ps*60)} X-10 E{round(Decimal(eValueresult),5)}\n")
        file.write(f"G1 E{round(Decimal(srd+ird*11),2) * -1} F{round(Decimal((srs+irs*loopbigcount) * 60),2)}\n")
        file.write(f"G0 F{int(ts)*60} Y10\n")
        file.write(f"G0 F{int(ts)*60} Y-10\n")
        file.write(f"G1 E{round(Decimal(srd+ird*11),2)} F{round(Decimal((srs+irs*loopbigcount) * 60),2)}\n")
        file.write(f"G1 F{int(ps*60)} X-10 E{round(Decimal(eValueresult),5)}\n")

        file.write(f"G1 F{int(ps*60)} X-1 E{round(Decimal(corenermarker),5)}\n")
        file.write(f"G1 F{int(ps*60)} Y1 E{round(Decimal(corenermarker),5)}\n")
        file.write(f"G1 F{int(ps*60)} X1 E{round(Decimal(corenermarker),5)}\n")
        file.write(f"G1 F{int(ps*60)} Y-1 E{round(Decimal(corenermarker),5)}\n")

        file.write(f"G1 F{int(ps*60)} Y-10 E{round(Decimal(eValueresult),5)}\n")
        file.write(f"G1 E{round(Decimal(srd+ird*12),2) * -1} F{round(Decimal((srs+irs*loopbigcount) * 60),2)}\n")
        file.write(f"G0 F{int(ts)*60} X-10\n")
        file.write(f"G0 F{int(ts)*60} X10\n")
        file.write(f"G1 E{round(Decimal(srd+ird*12),2)} F{round(Decimal((srs+irs*loopbigcount) * 60),2)}\n")
        file.write(f"G1 F{int(ps*60)} Y-10 E{round(Decimal(eValueresult),5)}\n")
        file.write(f"G1 E{round(Decimal(srd+ird*13),2) * -1} F{round(Decimal((srs+irs*loopbigcount) * 60),2)}\n")
        file.write(f"G0 F{int(ts)*60} X-10\n")
        file.write(f"G0 F{int(ts)*60} X10\n")
        file.write(f"G1 E{round(Decimal(srd+ird*13),2)} F{round(Decimal((srs+irs*loopbigcount) * 60),2)}\n")
        file.write(f"G1 F{int(ps*60)} Y-10 E{round(Decimal(eValueresult),5)}\n")
        file.write(f"G1 E{round(Decimal(srd+ird*14),2) * -1} F{round(Decimal((srs+irs*loopbigcount) * 60),2)}\n")
        file.write(f"G0 F{int(ts)*60} X-10\n")
        file.write(f"G0 F{int(ts)*60} X10\n")
        file.write(f"G1 E{round(Decimal(srd+ird*14),2)} F{round(Decimal((srs+irs*loopbigcount) * 60),2)}\n")
        file.write(f"G1 F{int(ps*60)} Y-10 E{round(Decimal(eValueresult),5)}\n")
        file.write(f"G1 E{round(Decimal(srd+ird*15),2) * -1} F{round(Decimal((srs+irs*loopbigcount) * 60),2)}\n")
        file.write(f"G0 F{int(ts)*60} X-10\n")
        file.write(f"G0 F{int(ts)*60} X10\n")
        file.write(f"G1 E{round(Decimal(srd+ird*15),2)} F{round(Decimal((srs+irs*loopbigcount) * 60),2)}\n")
        file.write(f"G1 F{int(ps*60)} Y-10 E{round(Decimal(eValueresult),5)}\n")

        file.write(f"G1 Z{lh}\n")

        layer = layer + 1

        for loopsmall in range(int(lt)):
            file.write(f";Layer {layer}\n")
            file.write(f"G1 F{int(ps*60)} X10 E{round(Decimal(eValueresult),5)}\n")
            file.write(f"G1 E{round(Decimal(srd+ird*0),2) * -1} F{round(Decimal((srs+irs*loopbigcount) * 60),2)}\n")
            file.write(f"G0 F{int(ts)*60} Y-10\n")
            file.write(f"G0 F{int(ts)*60} Y10\n")
            file.write(f"G1 E{round(Decimal(srd+ird*0),2)} F{round(Decimal((srs+irs*loopbigcount) * 60),2)}\n")
            file.write(f"G1 F{int(ps*60)} X10 E{round(Decimal(eValueresult),5)}\n")
            file.write(f"G1 E{round(Decimal(srd+ird*1),2) * -1} F{round(Decimal((srs+irs*loopbigcount) * 60),2)}\n")
            file.write(f"G0 F{int(ts)*60} Y-10\n")
            file.write(f"G0 F{int(ts)*60} Y10\n")
            file.write(f"G1 E{round(Decimal(srd+ird*1),2)} F{round(Decimal((srs+irs*loopbigcount) * 60),2)}\n")
            file.write(f"G1 F{int(ps*60)} X10 E{round(Decimal(eValueresult),5)}\n")
            file.write(f"G1 E{round(Decimal(srd+ird*2),2) * -1} F{round(Decimal((srs+irs*loopbigcount) * 60),2)}\n")
            file.write(f"G0 F{int(ts)*60} Y-10\n")
            file.write(f"G0 F{int(ts)*60} Y10\n")
            file.write(f"G1 E{round(Decimal(srd+ird*2),2)} F{round(Decimal((srs+irs*loopbigcount) * 60),2)}\n")
            file.write(f"G1 F{int(ps*60)} X10 E{round(Decimal(eValueresult),5)}\n")
            file.write(f"G1 E{round(Decimal(srd+ird*3),2) * -1} F{round(Decimal((srs+irs*loopbigcount) * 60),2)}\n")
            file.write(f"G0 F{int(ts)*60} Y-10\n")
            file.write(f"G0 F{int(ts)*60} Y10\n")
            file.write(f"G1 E{round(Decimal(srd+ird*3),2)} F{round(Decimal((srs+irs*loopbigcount) * 60),2)}\n")
            file.write(f"G1 F{int(ps*60)} X10 E{round(Decimal(eValueresult),5)}\n")

            file.write(f"G1 F{int(ps*60)} Y10 E{round(Decimal(eValueresult),5)}\n")
            file.write(f"G1 E{round(Decimal(srd+ird*4),2) * -1} F{round(Decimal((srs+irs*loopbigcount) * 60),2)}\n")
            file.write(f"G0 F{int(ts)*60} X10\n")
            file.write(f"G0 F{int(ts)*60} X-10\n")
            file.write(f"G1 E{round(Decimal(srd+ird*4),2)} F{round(Decimal((srs+irs*loopbigcount) * 60),2)}\n")
            file.write(f"G1 F{int(ps*60)} Y10 E{round(Decimal(eValueresult),5)}\n")
            file.write(f"G1 E{round(Decimal(srd+ird*5),2) * -1} F{round(Decimal((srs+irs*loopbigcount) * 60),2)}\n")
            file.write(f"G0 F{int(ts)*60} X10\n")
            file.write(f"G0 F{int(ts)*60} X-10\n")
            file.write(f"G1 E{round(Decimal(srd+ird*5),2)} F{round(Decimal((srs+irs*loopbigcount) * 60),2)}\n")
            file.write(f"G1 F{int(ps*60)} Y10 E{round(Decimal(eValueresult),5)}\n")
            file.write(f"G1 E{round(Decimal(srd+ird*6),2) * -1} F{round(Decimal((srs+irs*loopbigcount) * 60),2)}\n")
            file.write(f"G0 F{int(ts)*60} X10\n")
            file.write(f"G0 F{int(ts)*60} X-10\n")
            file.write(f"G1 E{round(Decimal(srd+ird*6),2)} F{round(Decimal((srs+irs*loopbigcount) * 60),2)}\n")
            file.write(f"G1 F{int(ps*60)} Y10 E{round(Decimal(eValueresult),5)}\n")
            file.write(f"G1 E{round(Decimal(srd+ird*7),2) * -1} F{round(Decimal((srs+irs*loopbigcount) * 60),2)}\n")
            file.write(f"G0 F{int(ts)*60} X10\n")
            file.write(f"G0 F{int(ts)*60} X-10\n")
            file.write(f"G1 E{round(Decimal(srd+ird*7),2)} F{round(Decimal((srs+irs*loopbigcount) * 60),2)}\n")
            file.write(f"G1 F{int(ps*60)} Y10 E{round(Decimal(eValueresult),5)}\n")

            file.write(f"G1 F{int(ps*60)} X-10 E{round(Decimal(eValueresult),5)}\n")
            file.write(f"G1 E{round(Decimal(srd+ird*8),2) * -1} F{round(Decimal((srs+irs*loopbigcount) * 60),2)}\n")
            file.write(f"G0 F{int(ts)*60} Y10\n")
            file.write(f"G0 F{int(ts)*60} Y-10\n")
            file.write(f"G1 E{round(Decimal(srd+ird*8),2)} F{round(Decimal((srs+irs*loopbigcount) * 60),2)}\n")
            file.write(f"G1 F{int(ps*60)} X-10 E{round(Decimal(eValueresult),5)}\n")
            file.write(f"G1 E{round(Decimal(srd+ird*9),2) * -1} F{round(Decimal((srs+irs*loopbigcount) * 60),2)}\n")
            file.write(f"G0 F{int(ts)*60} Y10\n")
            file.write(f"G0 F{int(ts)*60} Y-10\n")
            file.write(f"G1 E{round(Decimal(srd+ird*9),2)} F{round(Decimal((srs+irs*loopbigcount) * 60),2)}\n")
            file.write(f"G1 F{int(ps*60)} X-10 E{round(Decimal(eValueresult),5)}\n")
            file.write(f"G1 E{round(Decimal(srd+ird*10),2) * -1} F{round(Decimal((srs+irs*loopbigcount) * 60),2)}\n")
            file.write(f"G0 F{int(ts)*60} Y10\n")
            file.write(f"G0 F{int(ts)*60} Y-10\n")
            file.write(f"G1 E{round(Decimal(srd+ird*10),2)} F{round(Decimal((srs+irs*loopbigcount) * 60),2)}\n")
            file.write(f"G1 F{int(ps*60)} X-10 E{round(Decimal(eValueresult),5)}\n")
            file.write(f"G1 E{round(Decimal(srd+ird*11),2) * -1} F{round(Decimal((srs+irs*loopbigcount) * 60),2)}\n")
            file.write(f"G0 F{int(ts)*60} Y10\n")
            file.write(f"G0 F{int(ts)*60} Y-10\n")
            file.write(f"G1 E{round(Decimal(srd+ird*11),2)} F{round(Decimal((srs+irs*loopbigcount) * 60),2)}\n")
            file.write(f"G1 F{int(ps*60)} X-10 E{round(Decimal(eValueresult),5)}\n")

            file.write(f"G1 F{int(ps*60)} Y-10 E{round(Decimal(eValueresult),5)}\n")
            file.write(f"G1 E{round(Decimal(srd+ird*12),2) * -1} F{round(Decimal((srs+irs*loopbigcount) * 60),2)}\n")
            file.write(f"G0 F{int(ts)*60} X-10\n")
            file.write(f"G0 F{int(ts)*60} X10\n")
            file.write(f"G1 E{round(Decimal(srd+ird*12),2)} F{round(Decimal((srs+irs*loopbigcount) * 60),2)}\n")
            file.write(f"G1 F{int(ps*60)} Y-10 E{round(Decimal(eValueresult),5)}\n")
            file.write(f"G1 E{round(Decimal(srd+ird*13),2) * -1} F{round(Decimal((srs+irs*loopbigcount) * 60),2)}\n")
            file.write(f"G0 F{int(ts)*60} X-10\n")
            file.write(f"G0 F{int(ts)*60} X10\n")
            file.write(f"G1 E{round(Decimal(srd+ird*13),2)} F{round(Decimal((srs+irs*loopbigcount) * 60),2)}\n")
            file.write(f"G1 F{int(ps*60)} Y-10 E{round(Decimal(eValueresult),5)}\n")
            file.write(f"G1 E{round(Decimal(srd+ird*14),2) * -1} F{round(Decimal((srs+irs*loopbigcount) * 60),2)}\n")
            file.write(f"G0 F{int(ts)*60} X-10\n")
            file.write(f"G0 F{int(ts)*60} X10\n")
            file.write(f"G1 E{round(Decimal(srd+ird*14),2)} F{round(Decimal((srs+irs*loopbigcount) * 60),2)}\n")
            file.write(f"G1 F{int(ps*60)} Y-10 E{round(Decimal(eValueresult),5)}\n")
            file.write(f"G1 E{round(Decimal(srd+ird*15),2) * -1} F{round(Decimal((srs+irs*loopbigcount) * 60),2)}\n")
            file.write(f"G0 F{int(ts)*60} X-10\n")
            file.write(f"G0 F{int(ts)*60} X10\n")
            file.write(f"G1 E{round(Decimal(srd+ird*15),2)} F{round(Decimal((srs+irs*loopbigcount) * 60),2)}\n")
            file.write(f"G1 F{int(ps*60)} Y-10 E{round(Decimal(eValueresult),5)}\n")

            file.write(f"G1 Z{lh}\n")
            layer = layer + 1

        loopbigcount = loopbigcount + 1

    file.write(f"G1 Z5\n")
    file.write(f"G90\n")
    file.write(f"G28 X0 Y0\n")
    file.write(f"M84\n")
    file.write(f"M107\n")
    file.write(f"M104 S0\n")
    file.write(f"M140 S0\n")

    file.close()
