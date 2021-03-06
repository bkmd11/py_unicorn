""" This file is just text based pictures
    of unicorns. Very simple"""

basic_unicorn = """
                ^
                ^^
                ^^^
                ^^^^      A
                ^^^^^    AA
             AAAAAAAAAAAAAAA$$
          AAAAAAAAAAAAAAAAAA$$$
      AAAAAAAAA(  )AAAAAAAAA$$$$    
  AAAAAAAAAAAAAAAAAAAAAAAAAA$$$
  AAAAAAAAAAAAAAAAAAAAAAAAAA$$$$$$
              AAAAAAAAAAAAAA$$$$$
             AAAAAAAAAAAAAAA$$$$$$$
            AAAAAAAAAAAAAAAA$$$$$$$$
           AAAAAAAAAAAAAAAAA$$$$$$$$               
            """

chubby_unicorn = """
                      @.                         
                       ..                         
                  @@%/@,..@.@                     
                 ,...@. ...@....      @           
           &     @,...../......@   @*@            
            @       @.........         @          
          @            *... @            .        
         @                                @       
        @                                  @      
       @        @,*@  *@   &    #@@        .(     
       @      ,,,                 ,,,     ..@     
       @                                 ...@@,   
       @                               ....@,,,   
        @                            .....@.%,,.@ 
          @                      .......@    @@@  
             @@..................... @            
                 . @. @@@@(...@@.@                            
                """

fat_unicorn = """
                                         @
                                        @@        
                                       @@@          
                                  @    @          
                        ( @@(@%..,,@  /*,&        
                       , /,**,,..@  / *, @@       
                  %@,,.    ***@@@@      @   @     
                  @**,..   ,*@ @                @ 
               @,.,,***..  @@           ( )        @ @
               ,@*****,( @ @                          @
               @.,,**,                          @ @ @
              ****.%.                 /@    .@    
            @*,*,@@                       @       
          @,@,,  @                                
  @      #                      @           /     
  @,    #                                         
  %,,,  .@  @                  % @                
&@  ....,      @@.                          *     
   @,.., ,****@                            @      
       @.,**#@    .                      @  . @   
                        @@@@/      @@  
                         """

head_unicorn = """
                            ,           *
                            ,,         ***
                            ,,,         *                       
                            ,%,*(   %                   
                          ( /((((   /***                  
                      _ /          ****,                 
                 ___/          *****,,,,               * 
                /         @       *  ,,,,,/           ***   
                |                   ,,,////            *   
                 \\_____          /,////(((               
         *               /         /((((((/                
        ***             /        #((///// 
         *
        """

majestic_unicorn = """                                               
     @ 
      @@                                        
       @@ @@@@@@$                                 
        @@@@@@@@@$$                               
        @@@@@@@@@@$$$                             
       @@@   @@@@@@$$                            
             @@@@@@@@@@ /@@@@@   @@@@@           
            @@@@@@@@@@@@@@@@@@@@@@@@@@@$$       
            @@@@@@@@@@@@@@@@@@@@@(@@@@$$$$      
       @@@@@@@@@@@@@@@@@@@@@@@@@@@  %@@@@$$$$       
      @@       @@@@@@@@@@@@@   @@@@    @@@$$    
      @@       @@        @@&      @@     $$$$$$        
              @@          @@       @@            
              @            @         @           
             @            @           @@         
%           @@#          /@                       
%                                             
    """

kawaii_unicorn = """
                                                
                     @                            
                    *..@                          
                   @..@*.          &              
                   @.....@       @   %            
          @@      @..@@...@     @     @           
        @    @    ,......@,,,@ &  @   @           
       @   @   @*******,,*,,,,/  @    @           
       @    @/@******/,,,,*,,@/@    %&            
        @ &@*@*****@,,,,@%,,@@@    @              
         @@****@/       @@                        
            /               @&.  @    (           
            @    &&&   &   &&& &&&&               
            @   @&&/ &&%@  %&#&&#&%    @          
            @     @&&&@                @          
            @                                     
             @         @     @                    
              @(                    @@            
              &  @@              @....            
             @     .... @@@@ .........@           
            .          ...........     @          
          @                         (   @         
       @@@@    @                          @       
    @........@  ,                  %  @.......@   
    /.........@                    @ @.........@  
    @.........@  @        &       @ %..........@  
     @.......@    @...............   @........&   
                   @@@@@@( @@@#@@      @@...@  
    """

cat_unicorn = """
             @                                                                  
             *#@                                                                
             # *@                                                               
             * *(                                                               
  &.@@@      *@  ../                                                            
  ,*****@.*,@/.  @,,@             @@*  &*,,@                                    
 /,,******%.*@@. ,,,(@        @*    @**,**,@             #&@@&.                 
 @,********@.@,   @///@****@      @*******,@    @&                ...&@         
 @,,****%*    @/.../@//.         @,******,,@@                         ..*@      
  .,**@       @/.@.//%             @*****,,@*.   ......                 ..,**   
  @,%                .              .&*/,,,*...***&@@@@@@.*.              ..*(  
   @                 . . . ... . ..  *.@,,@*//@*,.  ,.    ,   *            .**# 
  @       @@.                        ..*&@***&**..                          .*(@
 @                         @          ..*@**,***...                         **# 
         /(              *(           ..**,**@***..                         (%%@
                               @      ..**@@@/.,,,.&@&**.                 .*%%%@
 @          %,,,,,,@                 .@/,,,,,,,,,,,,,... @,**          .,&%%(%%@
  @*.     @   *.  .               @&/////,,,,,,,,,,,,.........@&**,@@*###%%%%%@ 
  @**@*... #* **      &,......@///////////,,,,,,,,,  .......**********///%%%@#  
  @..***,@******,***@@,,,,,,,/////////@*     #/***/... . ... ,*******////%#.    
   ,....,******,@.,//////,////((((((@        ...@*,,,,, . .  *///////////*      
       &@#....*********@@/////*((((@@@      .......@#,,,,,,,,/////////@   
"""


def __text_keywords():
    """I look at all the variables in this file and return a keyword list for search hints"""
    global_vars = [i[0] for i in globals().items()]
    my_objects = [i for i in global_vars if '__' not in i]
    keywords = [i.split('_unicorn')[0] for i in my_objects]

    keywords.insert(0, 'Unicorn not found try:')

    return keywords
