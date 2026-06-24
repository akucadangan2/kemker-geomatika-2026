import geopandas as gpd

input_shp = r"E:\LOD KEMKER 2026\kirim\PERMUKIMAN_MERGE.shp"
output_geojson = r"E:\LOD KEMKER 2026\kirim\PERMUKIMAN_MERGE.geojson"

print("Membaca file shapefile...")
gdf = gpd.read_file(input_shp)

# 1. PAKSA DEFINISI KOORDINAT ASLI (UTM Zone 48S)
# EPSG 32748 adalah standar untuk wilayah barat/selatan Sumatera seperti Lampung
print("Menetapkan CRS sumber ke UTM 48S...")
gdf.set_crs(epsg=32748, allow_override=True, inplace=True)

# 2. KONVERSI KE WGS 84
print("Mengonversi sistem koordinat ke WGS 84 (EPSG:4326)...")
gdf = gdf.to_crs(epsg=4326)

print("Menyimpan ulang ke GeoJSON...")
gdf.to_file(output_geojson, driver="GeoJSON")

print("Berhasil! Silakan refresh Live Server Anda.")