from matplotlib.pyplot import xlabel
import plotly.express as px
import subprocess
from collections import Counter


def most_used_words( tweets ):
    #print( tweets )
    words = " ".join( tweets )
    words = words.lower()
    words = words.split()
    
    excluded_words = []

    with open("Analysis/100.txt","r") as read_file:
        for line in read_file.readlines():
            line = line.casefold()
            excluded_words.append(line[:len(line)-1])


    words = Counter( words )

    for word in excluded_words:
        if word in words:
            words.pop(word)
    
    #for tweet in tweets:
    #    words.update( tweet )

    print( words.most_common( 10 ) )

def period_activity( data, period_type ):
    dates = data.get( 'Date' )
    number_of_tweets = data.get( 'Number of Tweets' )

    ymax = max( number_of_tweets ) + 10
    ymin = min( number_of_tweets ) - 10
    xmax = dates[-1]
    xmin = dates[0]


    fig1 = px.scatter(
        data,
        x='Date',
        y='Number of Tweets',
        size='Number of Tweets',
        color='Number of Tweets',
        color_continuous_scale='Pinkyl'
    )

    fig1.update_layout(
        template = 'plotly_dark',
        coloraxis_showscale=False,
        yaxis_range=[ ymin,ymax ],
        xaxis_range=[ xmin,xmax ],
        title=period_type
    )

    fig1.write_html( f'Animations/{period_type}/{period_type}.html' )





    # fig1.show()




    for date in range( 1, 500 ):
    #for date in range( 1, len( data.get('Date') ) ):
        x = dates[0:date]
        y = number_of_tweets[0:date]
        fig = px.scatter(
            x=x,
            y=y,
            #size=y,
            color=y,
            range_color=[ymin,ymax],
            range_y=[ymin,ymax],
            color_continuous_scale='Peach',
        )

        fig.update_traces(
            marker=dict(
                size=15,
                sizemode='area',
                line=dict(width=0.5, color='black'),
                #sizeref=2.*max(number_of_tweets)/(40.**2),
                #sizemin=4
                )
            )
    
        fig.update_layout(
            template = 'plotly_dark',
            coloraxis_showscale=False,
            title=f'{ period_type }: { dates[ date ] }',
            yaxis_range=[ymin,ymax],
            xaxis_range=[xmin,xmax],
            xaxis_title='Date',
            yaxis_title='Number of Tweets'
        )
        fig.write_image( f'Animations/{period_type}/Frames/{date}.png', width=1920,height=1080 )
        print( f'Saved frame: { date } in DAILY ACTIVITY ANIMATION' )

    print( f'Animation {period_type} DONE' )