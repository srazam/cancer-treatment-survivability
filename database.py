import sqlalchemy as db
engine = db.create_engine("sqlite+pysqlite:///:memory:", echo=True)
features = ["radius_mean","texture_mean","perimeter_mean","area_mean","smoothness_mean","compactness_mean","concavity_mean",
            "concave points_mean","symmetry_mean","fractal_dimension_mean","radius_se","texture_se","perimeter_se","area_se",
            "smoothness_se","compactness_se","concavity_se","concave points_se","symmetry_se","fractal_dimension_se","radius_worst",
            "texture_worst","perimeter_worst","area_worst","smoothness_worst","compactness_worst","concavity_worst","concave points_worst",
            "symmetry_worst","fractal_dimension_worst"]

metadata_obj = db.MetaData()
patient_table = db.Table(
    'patient_info',
    metadata_obj,
    db.Column('id', db.String, primary_key=True),
    db.Column('diagnosis', db.String),
    *(db.Column(feat, db.Float) for feat in features),
)
metadata_obj.create_all(engine)

def add_patient_info(patient_info, patient_id, diag):
    with engine.begin() as connection:
        connection.execute(patient_table.insert().values(id=str(patient_id), diagnosis=str(diag), **patient_info))

def return_table():
    with engine.begin() as connection:
        return connection.execute(db.select(patient_table)).fetchall()