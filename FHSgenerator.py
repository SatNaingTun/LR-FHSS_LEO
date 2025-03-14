import galois
from src.families.LiFanMethod import LiFanFamily
from src.families.LR_FHSS_DriverMethod import LR_FHSS_DriverFamily
from src.families.LempelGreenbergMethod import LempelGreenbergFamily


# generate 3 families/sets of Frequency Hopping Sequences
# "lemgreen" for Lempel-Greenberger FHS family
# "driver" for LR-FHSS Driver FHS family
# "lifan" for Li-Fan FHS family
def get_FHSfamily(familyname, numGrids):

    # generate Lempel-Greenberger FHS family
    # Generated sequences have length q = p^n - 1
    # over an alphabet A of size |A| = p^k
    # for any given prime number p
    if familyname == "lemgreen":
        p = 2
        n = 5
        k = 5
        polys = galois.primitive_polys(p, n)
        poly1 = next(polys)
        lempelGreenbergFHSfam = LempelGreenbergFamily(p=p, n=n, k=k, poly=poly1)
        lempelGreenbergFHSfam.set_family(numGrids)
        return lempelGreenbergFHSfam.FHSfam

    # generate LR-FHSS Driver FHS family
    # parameter q is the length of the sequence (remind thses sequence have perdiod 35)
    # parameter regionDR is the region of the sequence, either "EU137", "EU336" or "US1523"
    elif familyname == "driver":
        driverFHSfam = LR_FHSS_DriverFamily(q=35, regionDR="EU137")
        return driverFHSfam.FHSfam


    # generate Li-Fan FHS family
    # parameter q is the length of the sequence
    # parameter maxfreq is the number of frequency channels
    # parameter mingap is the minimum gap between consecutive frequencies channels
    # methods "2l" and "3l" are available for generating Lifan FHS family
    elif familyname == "lifan":
        liFanFHSfam = LiFanFamily(q=34, maxfreq=280, mingap=8)
        liFanFHSfam.set_family(281, 8, '2l')
        return liFanFHSfam.FHSfam

    else:
        raise Exception(f"Invalid family name '{familyname}'")


if __name__ == "__main__":

    numGrids = 0            # number of LR-FHSS hopping grids
    familyname = "driver"   # FHS family name
    FHSfamily = get_FHSfamily(familyname, numGrids)
    
    export = True
    if export:
        filename = "driverEU137_FHSfamily.txt"
        with open(filename, 'w') as f:
            for fhs in FHSfamily:
                seq = ','.join(map(str, fhs))
                f.write(f"{seq}\n")

    else:
        for fhs in FHSfamily:
            print(fhs)




