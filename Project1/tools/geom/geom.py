from cyclops import *
from euclid import *
#geomModel = ModelGeometry.create('geom')
#getSceneManager().addModel(geomModel)

global numGeoms

def createGeoms(crimeObjs, colorDict):
    global numGeoms
    
    geomModel = ModelGeometry.create('geom')
    getSceneManager().addModel(geomModel)

    for crime in crimeObjs:
        geomModel.addVertex(crime.vector)
        c = colorDict[crime.primary]
        geomModel.addColor(Color(c))
        numGeoms += 1
        
    # create the geom shader
    geomProgram = ProgramAsset()
    geomProgram.name = "geoms"
    geomProgram.vertexShaderName = "geom.vert"
    geomProgram.fragmentShaderName = "geom.frag"
    geomProgram.geometryShaderName = "geom.geom"
    geomProgram.geometryOutVertices = 4
    geomProgram.geometryInput = PrimitiveType.Points
    geomProgram.geometryOutput = PrimitiveType.TriangleStrip
    getSceneManager().addProgram(geomProgram)
    
    # create the geoms
    sky = StaticObject.create('geoms')
    sky.getMaterial().setProgram('geoms')
    sky.getMaterial().setTransparent(True)
    sky.getMaterial().setAdditive(True)
    sky.getMaterial().setDepthTestEnabled(True)
    


    
'''
# create the geom shader
geomProgram = ProgramAsset()
geomProgram.name = "geoms"
geomProgram.vertexShaderName = "geom.vert"
geomProgram.fragmentShaderName = "geom.frag"
geomProgram.geometryShaderName = "geom.geom"
geomProgram.geometryOutVertices = 4
geomProgram.geometryInput = PrimitiveType.Points
geomProgram.geometryOutput = PrimitiveType.TriangleStrip
getSceneManager().addProgram(geomProgram)

# create the geoms
sky = StaticObject.create('geoms')
sky.getMaterial().setProgram('geoms')
sky.getMaterial().setTransparent(True)
sky.getMaterial().setAdditive(True)
sky.getMaterial().setDepthTestEnabled(True)
'''


'''
def runGeomProgram():

    # create the geom shader
    geomProgram = ProgramAsset()
    geomProgram.name = "geoms"
    geomProgram.vertexShaderName = "geom.vert"
    geomProgram.fragmentShaderName = "geom.frag"
    geomProgram.geometryShaderName = "geom.geom"
    geomProgram.geometryOutVertices = 4
    geomProgram.geometryInput = PrimitiveType.Points
    geomProgram.geometryOutput = PrimitiveType.TriangleStrip
    getSceneManager().addProgram(geomProgram)
    
    # create the geoms
    sky = StaticObject.create('geoms')
    sky.getMaterial().setProgram('geoms')
    sky.getMaterial().setTransparent(True)
    sky.getMaterial().setAdditive(True)
    sky.getMaterial().setDepthTestEnabled(True)
'''
    
