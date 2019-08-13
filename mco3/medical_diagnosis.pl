go :-
    nl, write('Skin disease diagnosis.'), nl,
    hypothesis(Disease),
    nl,
    format('Indeed, the patient does have ~w.', [Disease]).

go :-
    nl, write('Apologies. We cannot diagnose the disease.'), nl.

hypothesis(vitiligo) :-
    nl, write('Diagnosis for vitiligo.'), nl,
    symptom(patchy_skin),
    symptom(premature_whitening),
    symptom(tissue_color),
    symptom(retina_color).

hypothesis(acne) :-
    nl, write('Diagnosis for acne.'), nl,
    symptom(whiteheads),
    symptom(blackheads),
    symptom(pimples),
    symptom(papules),
    symptom(nodules),
    sympton(cystic_lesions).

hypothesis(cold_sore) :-
    nl, write('Diagnosis for cold sore.'), nl,
    symptom(tingling),
    symptom(blisters),
    symptom(oozing).

hypothesis(hives) :-
    nl, write('Diagnosis for hives.'), nl,
    symptom(flesh_colored),
    symptom(intensely_itchy),
    symptom(rougly_oval),
    symptom(one_inch).

hypothesis(latex_allergy) :-
    nl, write('Diagnosis for latex allergy.'), nl,
    symptom(itching),
    symptom(skin_redness),
    symptom(hives).

hypothesis(eczema) :-
    nl, write('Diagnosis for eczema.'), nl,
    symptom(dry_skin),
    symptom(itching),
    symptom(patches),
    symptom(bumps),
    symptom(scaly),
    symptom(scratching).

hypothesis(psoriasis) :-
    nl, write('Diagnosis for psoriasis.'), nl,
    symptom(red_patches),
    symptom(scaling),
    symptom(cracked_skin),
    symptom(soreness),
    symptom(ridged_nails),
    symptom(joints).

hypothesis(cellulitis) :-
    nl, write('Diagnosis for cellulitis.'), nl,
    symptom(blisters),
    symptom(red_area),
    symptom(swelling),
    symptom(tenderness),
    symptom(pain),
    symptom(warmth),
    symptom(fever),
    symptom(red_spots),
    symptom(skin_dimpling).

hypothesis(measles) :-
    nl, write('Diagnosis for measles.'), nl,
    symptom(fever),
    symptom(cough),
    symptom(conjunctivitis),
    symptom(runny_nose),
    symptom(rash).

hypothesis(basal_cell_carcinoma) :-
    nl, write('Diagnosis for basal cell carcinoma.'), nl,
    symptom(pink_bump),
    symptom(reddish_patch),
    symptom(blue_lesion),
    symptom(scar_lesion).

hypothesis(squamous_cell_carcinoma) :-
    nl, write('Diagnosis for squamous cell carcinoma.'), nl,
    symptom(red_nodule),
    symptom(flat_sore),
    symptom(new_sore),
    symptom(open_sore),
    symptom(red_sore),
    symptom(raise_patch).

response(Reply) :-
    read(Reply).

symptom(patchy_skin) :-
    write('Does the patient have patchy loss of skin? (y/n) '),
    response(Reply),
    Reply='y'.

symptom(premature_whitening) :-
    write('Does the patient have premature whitening of hair on scalp, eyelashes, eyebrows, and/or beard? (y/n) '),
    response(Reply),
    Reply='y'.

symptom(tissue_color) :-
    write('Does the patient suffer from loss of color in the tissues that line the inside of your mouth and nose (mucous membranes)? (y/n) '),
    response(Reply),
    Reply='y'.

symptom(retina_color) :-
    write('Does the patient suffer from loss of or change in color of the inner layer of the eyeball (retina)? (y/n) '),
    response(Reply),
    Reply='y'.

symptom(whiteheads) :-
    write('Does the patient have closed plugged pores? (y/n) '),
    response(Reply),
    Reply='y'.

symptom(blackheads) :-
    write('Does the patient have open plugged pores? (y/n) '),
    response(Reply),
    Reply='y'.

symptom(pimples) :-
    write('Does the patient have pimples? (y/n) '),
    response(Reply),
    Reply='y'.

symptom(papules) :-
    write('Does the patient have papules? (y/n) '),
    response(Reply),
    Reply='y'.

symptom(nodules) :-
    write('Does the patient have large, solid, painful lumps beneath the surface of the skin? (y/n) '),
    response(Reply),
    Reply='y'.

symptom(cystic_lesion) :-
    write('Does the patient have painful, pus-filled lumps beneath the surface of the skin? (y/n) '),
    response(Reply),
    Reply='y'.

symptom(tingling) :-
    write('Does the patient suffer from itching? (y/n) '),
    response(Reply),
    Reply='y'.

symptom(blisters) :-
    write('Does the patient have blisters? (y/n) '),
    response(Reply),
    Reply='y'.

symptom(oozing) :-
    write('Does the patient have oozing and crusting? (y/n) '),
    response(Reply),
    Reply='y'.

symptom(flesh_colored) :-
    write('Does the patient\'s welts have red or flesh color? (y/n) '),
    response(Reply),
    Reply='y'.

symptom(intensely_itchy) :-
    write('Are the patient\'s welts intensely itchy? (y/n) '),
    response(Reply),
    Reply='y'.

symptom(rougly_oval) :-
    write('Are the patient\'s welts roughly oval or shaped like a worm? (y/n) '),
    response(Reply),
    Reply='y'.

symptom(one_inch) :-
    write('Are the patient\'s welts less than one inch? (y/n) '),
    response(Reply),
    Reply='y'.

symptom(itching) :-
    write('Does the patient suffer from itching? (y/n) '),
    response(Reply),
    Reply='y'.

symptom(skin_redness) :-
    write('Does the patient suffer from skin redness? (y/n) '),
    response(Reply),
    Reply='y'.

symptom(hives) :-
    write('Does the patient have hives? (y/n) '),
    response(Reply),
    Reply='y'.

symptom(dry_skin) :-
    write('Does the patient have dry skin? (y/n) '),
    response(Reply),
    Reply='y'.

symptom(patches) :-
    write('Does the patient have red to brownish-gray patches, especially on the hands, feet, ankles, wrists, neck, upper chest, eyelids, inside the bend of the elbows and knees? (y/n) '),
    response(Reply),
    Reply='y'.

symptom(bumps) :-
    write('Does the patient have small, raised bumps, which may leak fluid and crust over when scratched? (y/n) '),
    response(Reply),
    Reply='y'.

symptom(scaly) :-
    write('Does the patient have thickened, cracked, scaly skin? (y/n) '),
    response(Reply),
    Reply='y'.

symptom(scratching) :-
    write('Does the patient have raw, sensitive, swollen skin from scratching? (y/n) '),
    response(Reply),
    Reply='y'.

symptom(red_patches) :-
    write('Does the patient have red patches of skin covered with thick, silvery scales? (y/n) '),
    response(Reply),
    Reply='y'.

symptom(scaling) :-
    write('Does the patient have small scaling spots? (y/n) '),
    response(Reply),
    Reply='y'.

symptom(cracked_skin) :-
    write('Does the patient have dry, cracked skin that may bleed? (y/n) '),
    response(Reply),
    Reply='y'.

symptom(soreness) :-
    write('Does the patient have itching, burning or soreness? (y/n) '),
    response(Reply),
    Reply='y'.

symptom(ridged_nails) :-
    write('Does the patient have ridged nails? (y/n) '),
    response(Reply),
    Reply='y'.

symptom(joints) :-
    write('Does the patient have swollen joints? (y/n) '),
    response(Reply),
    Reply='y'.

symptom(red_area) :-
    write('Does the patient have a red area of skin that tends to expand? (y/n) '),
    response(Reply),
    Reply='y'.

symptom(swelling) :-
    write('Does the patient have a swelling? (y/n) '),
    response(Reply),
    Reply='y'.

symptom(tenderness) :-
    write('Does the patient suffer from tenderness? (y/n) '),
    response(Reply),
    Reply='y'.

symptom(pain) :-
    write('Does the patient suffer from pain? (y/n) '),
    response(Reply),
    Reply='y'.

symptom(warmth) :-
    write('Does the patient have warmth? (y/n) '),
    response(Reply),
    Reply='y'.

symptom(fever) :-
    write('Does the patient have fever? (y/n) '),
    response(Reply),
    Reply='y'.

symptom(red_spots) :-
    write('Does the patient have red spots? (y/n) '),
    response(Reply),
    Reply='y'.

symptom(skin_dimpling) :-
    write('Does the patient have skin dimpling? (y/n) '),
    response(Reply),
    Reply='y'.

symptom(cough) :-
    write('Does the patient have cough? (y/n) '),
    response(Reply),
    Reply='y'.

symptom(conjunctivitis) :-
    write('Does the patient have conjunctivitis? (y/n) '),
    response(Reply),
    Reply='y'.

symptom(runny_nose) :-
    write('Does the patient have runny nose? (y/n) '),
    response(Reply),
    Reply='y'.

symptom(rash) :-
    write('Does the patient have rash? (y/n) '),
    response(Reply),
    Reply='y'.

symptom(pink_bump) :-
    write('Does the patient have a white, waxy, scar-like lesion? (y/n) '),
    response(Reply),
    Reply='y'.

symptom(reddish_patch) :-
    write('Does the patient have a flat, scaly, reddish patch? (y/n) '),
    response(Reply),
    Reply='y'.

symptom(blue_lesion) :-
    write('Does the patient have a brown, black, or blue lesion? (y/n) '),
    response(Reply),
    Reply='y'.

symptom(scar_lesion) :-
    write('Does the patient have a white, waxy, scar-like lesion? (y/n) '),
    response(Reply),
    Reply='y'.

symptom(red_nodule) :-
    write('Does the patient have a firm, red nodule? (y/n) '),
    response(Reply),
    Reply='y'.

symptom(flat_sore) :-
    write('Does the patient have a flat sore with a scaly crust? (y/n) '),
    response(Reply),
    Reply='y'.

symptom(new_sore) :-
    write('Does the patient have a new sore or raised area on an old scar or ulcer? (y/n) '),
    response(Reply),
    Reply='y'.

symptom(open_sore) :-
    write('Does the patient have a rough, scaly patch on your lip that may evolve to an open sore? (y/n) '),
    response(Reply),
    Reply='y'.

symptom(red_sore) :-
    write('Does the patient have a red sore or rough patch inside their mouth? (y/n) '),
    response(Reply),
    Reply='y'.

symptom(raise_patch) :-
    write('Does the patient have a red, raised patch or wartlike sore on or in the anus or on their genitals? (y/n) '),
    response(Reply),
    Reply='y'.
