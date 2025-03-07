from django.http import HttpResponse
import subprocess
import datetime
import pytz

def htop(request):
    name = 'Mahak'
    username = subprocess.getoutput('whoami')
    server_time = datetime.datetime.now(pytz.timezone('Asia/Kolkata')).strftime('%Y-%m-%d %H:%M:%S')
    top_output = subprocess.getoutput('top -b -n 1 | head -n 20')

    response = f'''
    <pre>
    Name: {name}
    Username: {username}
    Server Time (IST): {server_time}
    Top Output:
    {top_output}
    </pre>
    '''
    return HttpResponse(response)