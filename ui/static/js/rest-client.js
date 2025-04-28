async function send_async_get_request() {
    const result = await fetch("/api/v1/tasks/")
    const jsonResult = await result.json()
    console.log(jsonResult)
}

send_async_get_request()

async function send_async_put_request() {
    const result = await fetch("/api/v1/tasks/", 
        { 
            method: "put", 
            body: JSON.stringify({ id: 12, title: "finish the dishes on time!"}),
            headers: {
                "Content-Type": "application/json",
            },
        }
    )  
    
    const jsonResult = await result.json()
    console.log(jsonResult)
}

send_async_put_request()