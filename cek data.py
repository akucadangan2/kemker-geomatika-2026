import geopandas as gpd

input_shp = r"E:\LOD KEMKER 2026\kirim\PERMUKIMAN_MERGE.shp"
output_geojson = r"E:\LOD KEMKER 2026\kirim\PERMUKIMAN_MERGE_CLEAN.geojson"

try:
    print("Membaca file shapefile...")
    gdf = gpd.read_file(input_shp)
    
    # Menetapkan CRS asli (UTM Zone 48S)
    gdf.set_crs(epsg=32748, allow_override=True, inplace=True)

    print("\n--- Analisis Atribut Sebelum Pembersihan ---")
    print(f"Jumlah kolom awal: {len(gdf.columns)}")

    # 1. MENGHAPUS KOLOM KOSONG
    # Menghapus kolom yang seluruh barisnya kosong (NaN/None)
    # Ini memastikan kita hanya membawa data autentik ke WebGIS
    gdf_clean = gdf.dropna(axis=1, how='all')
    
    print(f"Jumlah kolom setelah dibersihkan: {len(gdf_clean.columns)}")
    print("Kolom yang dipertahankan:", gdf_clean.columns.tolist())

    # 2. MENAMBAHKAN ATRIBUT TINGGI BANGUNAN
    # Menambahkan kolom 'TINGGI' dengan nilai default 3 meter
    # agar bisa langsung dibaca oleh sistem LOD 1 di HTML
    gdf_clean = gdf_clean.assign(TINGGI=3.0)
    print("\nAtribut 'TINGGI' (3.0 meter) berhasil ditambahkan.")

    # 3. KONVERSI CRS KE WGS 84
    print("\nMengonversi ke WGS 84 (EPSG:4326)...")
    gdf_clean = gdf_clean.to_crs(epsg=4326)

    # 4. MENYIMPAN HASIL KE GEOJSON BARU
    print("Menyimpan ke GeoJSON yang sudah bersih...")
    gdf_clean.to_file(output_geojson, driver="GeoJSON")
    
    print(f"\nSelesai! File bersih disimpan sebagai: PERMUKIMAN_MERGE_CLEAN.geojson")

except Exception as e:
    print(f"Terjadi kesalahan: {e}")