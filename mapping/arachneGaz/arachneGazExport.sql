SELECT DISTINCT arachneentityidentification.ArachneEntityID, ort.Gazetteerid
FROM objektplastik, ortsbezug, ort, arachneentityidentification
WHERE objektplastik.PS_ObjektplastikID = ortsbezug.FS_ObjektID AND ortsbezug.FS_OrtID = ort.PS_OrtID AND arachneentityidentification.ForeignKey = objektplastik.PS_ObjektplastikID AND arachneentityidentification.TableName LIKE "objekt" AND (ortsbezug.ArtOrtsangabe LIKE "%Fundort%" OR ortsbezug.ArtOrtsangabe LIKE "%site%" OR ortsbezug.ArtOrtsangabe LIKE "%antik%" OR ortsbezug.ArtOrtsangabe LIKE "%Herkunftsort%“);
