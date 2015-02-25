import web
from tool import is_valid, get_results

urls = (
    '/', 'index',
    '/query', 'query',
)
app = web.application(urls, globals())
render = web.template.render('templates/')

class index:
    def GET(self):
        return render.index()

class query:        
    def POST(self):
        i = web.input()
        if not i.has_key('board'):
            return "error: malformed request (expecting 'board' field)"

        board = i.board.replace('\r', '')

        valid, reason = is_valid(board)
        if not valid:
            return "error: not a valid board, " + reason

        results = get_results(board)
        return '\n\n'.join(results)

if __name__ == "__main__":
    app.run()
