<script type="text/javascript"> 
    $(function() { 
        $("#btn_1").click(function() { 
            var $keyword = $("#Text1").val() 
            setHeightKeyWord('bbb', $keyword, 'Red', true) 
        }); 
    }); 
    function setHeightKeyWord(id, keyword, color, bold) { 
        if (keyword == "") 
            return; 
        var tempHTML = $("#" + id).html(); 
        var htmlReg = new RegExp("\<.*?\>", "i"); 
        var arrA = new Array(); 
        for (var i = 0; true; i++) { 
            var m = htmlReg.exec(tempHTML); 
            if (m) { 
                arrA[i] = m; 
            } 
            else { 
                break; 
            } 
            tempHTML = tempHTML.replace(m, "[[[[" + i + "]]]]"); 
        } 
        var replaceText 
        if (bold) 
            replaceText = "<b style='color:" + color + ";'>$1</b>"; 
        else 
            replaceText = "<font style='color:" + color + ";'>$1</font>"; 
        var arrayWord = keyword.split(','); 
        for (var w = 0; w < arrayWord.length; w++) { 
            var r = new RegExp("(" + arrayWord[w].replace(/[(){}.+*?^$|\\\[\]]/g, "\\$&") + ")", "ig"); 
            tempHTML = tempHTML.replace(r, replaceText); 
        } 
        for (var i = 0; i < arrA.length; i++) { 
            tempHTML = tempHTML.replace("[[[[" + i + "]]]]", arrA[i]); 
        } 
        $("#" + id).html(tempHTML); 
    } 
</script>
