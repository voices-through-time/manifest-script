# Bulk uploading files to Zooniverse

When uploading archive records to Zooniverse it is important to use a manifest which will ensure that each record has the approriate data associated with it.

As description of what a manifest is and why it is important can be found [here](https://help.zooniverse.org/getting-started/example/#details-subject-sets-and-manifest-details-aka-what-is-a-manifest)

This script, when the script is run within this directory, it will iterate through each record found in the directory prescribed in the *path* variable, and create a csv file with the appririate information.

Information that is important to include is the subject number,internal_id,title,group_id,volume,date range,source,owner,filename.

The date name will change for each volume, and details for this can be found on the drive.

The source and owner will stay the same.

The number is the number of the record, which is within the filename.

The filename is simply the filename.

## What is the internal_id and group_id for?

These are important for using the [ALICE](https://alice.zooniverse.org/about) tool, in which mutiple transcriptions of free text can be aggregated.

Where written documents span over multiple digital records (e.g a three page letter) it is important to transcribe them as a group. Where this happens within Coram records, filenames will contain letters in the end of the name. E.G 
within the Petitions Admitted and Rejected for Ballot record group there are two:

petitions_admitted_and_rejected_004_092

one has the filename petitions_admitted_and_rejected_004_092_a1
and the other petitions_admitted_and_rejected_004_092_a2.

Both of these that the group_id petitions_admitted_and_rejected_004_092 to that they can be reveied together.

Where records do not have this nomucature, (where records are not grouped over pages) the group_id can match the volumne name.

Eg, in the Subcomittie minuites record group, all those within Volume 6 will have the group_id 'A_FH_A_03_005_006'


