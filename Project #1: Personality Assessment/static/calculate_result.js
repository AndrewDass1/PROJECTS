function result() 
{
    var total_score=0;

    var sad_counter=0;
    var angry_counter=0;
    var neutral_counter=0;
    var elated_counter=0;


    if(document.getElementById('1a').checked)
    {	
        elated_counter = elated_counter + 1;
        total_score = total_score + 1;
    }
    if(document.getElementById('1b').checked)
    {	
        sad_counter = sad_counter + 1;
        total_score = total_score + 1;
    }
    if(document.getElementById('1c').checked)
    {	
        neutral_counter = neutral_counter + 1;
        total_score = total_score + 1;
    }
    if(document.getElementById('1d').checked)
    {	
        angry_counter = angry_counter + 1;
        total_score = total_score + 1;
    }


    if(document.getElementById('2a').checked)
    {	
        neutral_counter = neutral_counter + 1;
        total_score = total_score + 1;
    }
    if(document.getElementById('2b').checked)
    {	
        sad_counter = sad_counter + 1;
        total_score = total_score + 1;
    }
    if(document.getElementById('2c').checked)
    {	
        elated_counter = elated_counter + 1;
        total_score = total_score + 1;
    }
    if(document.getElementById('2d').checked)
    {	
        angry_counter = angry_counter + 1;
        total_score = total_score + 1;
    }


    if(document.getElementById('3a').checked)
    {	
        sad_counter = sad_counter + 1;
        total_score = total_score + 1;
    }
    if(document.getElementById('3b').checked)
    {	
        elated_counter = elated_counter + 1;
        total_score = total_score + 1;
    }
    if(document.getElementById('3c').checked)
    {	
        neutral_counter = neutral_counter + 1;
        total_score = total_score + 1;
    }
    if(document.getElementById('3d').checked)
    {	
        angry_counter = angry_counter + 1;
        total_score = total_score + 1;
    }


    if(document.getElementById('4a').checked)
    {	
        elated_counter = elated_counter + 1;
        total_score = total_score + 1;
    }
    if(document.getElementById('4b').checked)
    {	
        sad_counter = sad_counter + 1;
        total_score = total_score + 1;
    }
    if(document.getElementById('4c').checked)
    {	
        neutral_counter = neutral_counter + 1;
        total_score = total_score + 1;
    }
    if(document.getElementById('4d').checked)
    {	
        angry_counter = angry_counter + 1;
        total_score = total_score + 1;
    }


    if(document.getElementById('5a').checked)
    {	
        angry_counter = angry_counter + 1;
        total_score = total_score + 1;
    }
    if(document.getElementById('5b').checked)
    {	
        elated_counter = elated_counter + 1;
        total_score = total_score + 1;
    }
    if(document.getElementById('5c').checked)
    {	
        neutral_counter = neutral_counter + 1;
        total_score = total_score + 1;
    }
    if(document.getElementById('5d').checked)
    {	
        sad_counter = sad_counter + 1;
        total_score = total_score + 1;
    }

    if(document.getElementById('6a').checked)
    {	
        neutral_counter = neutral_counter + 1;
        total_score = total_score + 1;
    }
    if(document.getElementById('6b').checked)
    {	
        elated_counter = elated_counter + 1;
        total_score = total_score + 1;
    }
    if(document.getElementById('6c').checked)
    {	
        angry_counter = angry_counter + 1;
        total_score = total_score + 1;
    }
    if(document.getElementById('6d').checked)
    {	
        sad_counter = sad_counter + 1;
        total_score = total_score + 1;
    }


    if(document.getElementById('7a').checked)
    {	
        elated_counter = elated_counter + 1;
        total_score = total_score + 1;
    }
    if(document.getElementById('7b').checked)
    {	
        neutral_counter = neutral_counter + 1;
        total_score = total_score + 1;
    }
    if(document.getElementById('7c').checked)
    {	
        angry_counter = angry_counter + 1;
        total_score = total_score + 1;
    }
    if(document.getElementById('7d').checked)
    {	
        sad_counter = sad_counter + 1;
        total_score = total_score + 1;
    }

    if(document.getElementById('8a').checked)
    {	
        angry_counter = angry_counter + 1;
        total_score = total_score + 1;
    }
    if(document.getElementById('8b').checked)
    {	
        elated_counter = elated_counter + 1;
        total_score = total_score + 1;
    }
    if(document.getElementById('8c').checked)
    {	
        neutral_counter = neutral_counter + 1;
        total_score = total_score + 1;
    }
    if(document.getElementById('8d').checked)
    {	
        sad_counter = sad_counter + 1;
        total_score = total_score + 1;
    }

    if(document.getElementById('9a').checked)
    {	
        elated_counter = elated_counter + 1;
        total_score = total_score + 1;
    }
    if(document.getElementById('9b').checked)
    {	
        sad_counter = sad_counter + 1;
        total_score = total_score + 1;
    }
    if(document.getElementById('9c').checked)
    {	
        neutral_counter = neutral_counter + 1;
        total_score = total_score + 1;
    }
    if(document.getElementById('9d').checked)
    {	
        angry_counter = angry_counter + 1;
        total_score = total_score + 1;
    }


    if(document.getElementById('10a').checked)
    {	
        neutral_counter = neutral_counter + 1;
        total_score = total_score + 1;
    }
    if(document.getElementById('10b').checked)
    {	
        elated_counter = elated_counter + 1;
        total_score = total_score + 1;
    }
    if(document.getElementById('10c').checked)
    {	
        angry_counter = angry_counter + 1;
        total_score = total_score + 1;
    }
    if(document.getElementById('10d').checked)
    {	
        sad_counter = sad_counter + 1;
        total_score = total_score + 1;
    }
                    
                    
    if ( total_score == 10 && sad_counter >= angry_counter && sad_counter >= neutral_counter && sad_counter >= elated_counter)
    {
        location.replace("/sad")
    }
    if ( total_score == 10 && angry_counter >= sad_counter && angry_counter >= neutral_counter && angry_counter >= elated_counter )
    {
        location.replace("/angry")
    }
    if ( total_score == 10 && neutral_counter >= sad_counter && neutral_counter >= angry_counter && neutral_counter >= elated_counter )
    {
        location.replace("/neutral")
    }
    if ( total_score == 10 && elated_counter >= sad_counter && elated_counter >= angry_counter && elated_counter >= neutral_counter)
    {
        location.replace("/elated")
    }
                    
}
                    