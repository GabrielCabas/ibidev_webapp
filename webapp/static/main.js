$("#send_button").on("click", ()=>{
    $.ajax({
        url: "/",
        type: "POST",
        data: {
            "message": $("#input_text").val()
        }
    }).then((res)=>{
        console.log(res)
    })
})