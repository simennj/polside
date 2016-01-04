USE polguide;
DELETE FROM pol_bolitems;
LOAD XML LOCAL INFILE 'bol.xml' INTO TABLE pol_bolitems;