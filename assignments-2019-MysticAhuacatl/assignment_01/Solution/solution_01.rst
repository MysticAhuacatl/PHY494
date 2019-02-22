.. -*- coding: utf-8 -*-

====================
 PHY494 Solution 01
====================

Copyright © 2016, 2017, 2018 Ian Kenney, Oliver Beckstein. ALL RIGHTS
RESERVED. These solutions can ONLY be used by current students of the
ASU PHY494 Class "Computational Methods in Physics". DISSEMINATION IN
ANY FORM IS PROHIBITED.

.. Note: If you read this document as a plain text file then please be
.. aware that it is written in "restructured text" and contains some
.. text markup. For instance, code is written within backticks like
.. this: ``ls $HOME``. These backticks are *not* part of the solution.


(See *assignment_01.pdf* for the detailed break-down of points.)

1.1 Commands and paths (8 points)
=================================

a) What is the function of the cd and the pwd command?

   - ``cd``    : change directory
   - ``pwd``   : print the present working directory

b) Show commands for two different ways to change to your home directory,
   assuming you are currently in the root directory.

   Possible solutions:

   - ``cd``
   - ``cd $HOME``
   - ``cd ~``
   - ``cd ~$USER``
   - ``cd /home/$USER``
   - ``cd home/$USER`` (works because you are in the root directory ``/``)
   - ``cd home/../home/../home/../home/../home/../home/$USER` (kind of a joke)     

c) Given the path ``/home/dvader/Documents/../data/bases``:

   i) Is this an absolute path or relative path?
   
      - Absolute

  ii) If you are located in the home directory of user dvader
      (``/home/dvader``) then what is the shortest path to bases?
      
      - ``data/bases``

d) If you were in a directory ``/home/dvader/data`` and you executed the
   command ``cd ./.././.././.``, what would be the output of running the
   pwd command afterwards? [1]_
    
       - ``/home``
       
.. [1] Sorry if you got confused by the comma in the question after
       the path... lesson: every little detail counts in Unix.

e) Describe two ways by which you could learn more about the function
   of a Unix command ``frbzz`` that you don't know anything about.

       1. **Manual page**: Looking for a man page entry for the command in question (``man frbzz``)
       2. **Help flags**: Try some typical flags for help (``frbzz -h``, ``frbzz --help``)
       3. **Search on the internet**: Google it... (do not
 	  underestimate how useful this is!)

f) BONUS (+4*)

   - Advantages
   
         - actions are not limited by the design of the user interface
         - fast (once you master it)
         - modular (chaining of many small, well-designed and
           powerful tools with pipes)
         - shell glob patterns and regular expressions make it easy to
           work with large numbers of files
         - scripts as libraries of solutions to recurring tasks
         - batch processing of large number of files
         - can be used remotely even over poor connections
         - small resource footprint (available on *anything*)
         - clearer picture of filesystem structure
         - You look flippin' awesome in starbucks [2]_
           
   - Disadvantages
   
         - steep learning curve (unintuitive)
         - unforgiving
         - It is "ugly" [2]_
         - Little mouse support
         - Little color support
         - no support for graphics or working with images
         - Coffee shop owners think you are a cyber terrorist (says Ian)

.. [2] This statement is "in the eye of the beholder..."


1.2 Copy, rename, delete (4 points)
===================================

Show the output of the commands::

  cd ~
  ls -R PHY494/01_shell
  
which will be compared against the expected directory structure and
content.

Expected output::
    
   |============================================================|
   |01_shell/:                                                  |
   |         Documents  data                                    |
   |                                                            |
   |01_shell/Documents:                                         |
   |         work                                               |
   |                                                            |
   |01_shell/Documents/work:                                    |
   |         TODO.bak  TODO.txt  hints.txt  lesson.txt          |
   |                                                            |
   |01_shell/data:                                              |
   |         notes                                              |
   |                                                            |
   |01_shell/data/notes:                                        |
   |         TODO.txt                                           |
   |============================================================|


1.3 Danger Zone (3 points)
==========================


Describe what the command ``rm -rf /`` might do. Should you ever use
it? ::

	rm -rf /
	^   ^^ ^
	|   || +-- root directory / top level directory
	|   |+---- force (no prompts) 
	|   +----- recursive (until it reaches the end)
	+--- Remove command


- It will *recursively* (option ``-r``) delete *all* directories and
  all files and directories in these directories, starting from the
  root directory ``/``. With the "force" option (``-f``) it will also
  *not* prompt for any confirmations.
- I should never use this command (because it will likely leave my
  computer in a broken state and everything will be gone).

   
1.4 BONUS: Pipes and Filters (+5* points)
=========================================

a) How many lines does the file ``planets_2.dat`` contain?

   - Command::

        wc planets_2.dat
        
   - Output::
   
      |=============================|
      | 120  360 5888 planets_2.dat |
      |=============================|

   - Answer: 120 lines
      
b) What are the three biggest planets (by diameter) in the file
   ``planets.dat``?

   - Command::

        sort planets.dat -k2 -nr | head -3
        
   - Output::

      |============================================================|
      |Bespin              118000  gasgiant                        |
      |Kamino               19720  ocean                           |
      |Malastare            18880  swamps/deserts/jungles/mountains|
      |============================================================|

   - Answer: Bespin, Kamino, Malastare
      
c) Which planets contain ice terrain?

   - Command::

          grep ice planets.dat
          
   - Output (if you also include planets with glacier terrain then
     that will count, too)::

      |==========================================================|
      |Hoth                  7200  tundra/icecaves/mountainranges|
      |Mygeeto              10088  glaciers/mountains/icecanyons |
      |==========================================================|

   - Answer: Hoth, Mygeeto

d) What is the most frequent and the least frequent first letter
   amongst all the planets?

   - Command::

         cut -b 1 planets.dat | sort | uniq -c | sort -r
         
   - Output::
   
      |=========|
      |   7 S   |
      |   7 C   |
      |   6 T   |
      |   6 M   |
      |   4 D   |
      |   3 K   | 
      |   2 U   |
      |   2 R   |
      |   2 O   |
      |   2 N   |
      |   2 I   |
      |   2 H   |
      |   2 G   |
      |   2 E   |
      |   2 B   |
      |   2 A   |
      |   1 Z   |
      |   1 Y   |
      |   1 V   |
      |   1 Q   |
      |   1 P   |
      |   1 J   |
      |   1 F   |
      |=========|

   - Answer: "S" and "C" are most frequent, "Z", "Y", "V", "Q". "P",
     "J", "F" are least frequent (but not 0)     
