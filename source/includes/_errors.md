# 错误代码

<aside class="notice">
APIGPT APIs 使用下列的错误代码
</aside>



Error Code | Meaning
---------- | -------
400 | Invalid request: there was an issue with the format or content of your request.
401 | Unauthorized: there's an issue with your API key.
403 | Forbidden: your API key does not have permission to use the specified resource.
404 | Not found: the requested resource was not found.
429 | Your account has hit a rate limit.
500 | An unexpected error has occurred internal to Anthropic's systems.
529 | Your API is temporarily overloaded.

When receiving a streaming response via SSE, it's possible that an error can occur after returning a 200 response, in which case error handling wouldn't follow these standard mechanisms.


