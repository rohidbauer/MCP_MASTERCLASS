from fastmcp import FastMCP

mcp = FastMCP()

@mcp.tool()
def fetch():
    '''Use this tools to fetch data from a source.'''

    # Simulate fetching data from a source.
    ''' You can make some API calls here or fetch data from a database. '''
    return {"data": "Hello, MCP!"}
@mcp.tool()
def process():
    '''Use this tools to processed the fetch data.'''

    # Simulate processing the fetched data.
    ''' You can perform some data transformations here '''
    return{"processed_data": "Data has been processed!"}

if __name__ == "__main__":
    # Run the MCP server
    mcp.run(transport="stdio")