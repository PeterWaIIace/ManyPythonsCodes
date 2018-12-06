#!/bin/bash
listoperation='add sub mul div'
select operation in $listoperation
do
if [ $operation = 'add' ]
then 
echo "enter first value: "
read firstvalue
echo "enter second value: "
read secondvalue
expr $firstvalue + $secondvalue
elif [ $operation = 'sub' ]
then
echo "enter first value: "
read firstvalue
echo "enter second value: "
read secondvalue
expr $firstvalue - $secondvalue    
elif [ $operation = 'mul' ]
then
echo "enter first value: "
read firstvalue
echo "enter second value: "
read secondvalue
expr $firstvalue \* $secondvalue    
elif [ $operation = 'div' ]
then
echo "enter first value: "
read firstvalue
echo "enter second value: "
read secondvalue
expr $firstvalue / $secondvalue    
fi
done

