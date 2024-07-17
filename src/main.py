import sys
import os
from src.app.cs.cs_writer_config import CSWriterConfig
from src.app.utility.file_store import FileStore
from src.app.engine.script_engine import ScriptEngine
from src.app.cs.cs_engine import CSEngine

from src.app.utility.file_util import read_file_store
from src.app.utility.file_util import move_file_store


if __name__ == "__main__":
    sourceFolder = r"C:\RVA\prj\intefict-data"
    sourceFile = "house_tutorial.txt"
    targetFolder = r"C:\RVA\prj\intefict-data\Choicescript\choicescript-main\web\mygame\scenes"
    targetFile = "story.txt"
    if len(sys.argv) < 3:
        print("Please provide sourceFolder and targetFolder as command line arguments.")
        #sys.exit(1)
    else:
        sourceFolder = sys.argv[1]
        targetFolder = sys.argv[2]

    
    
    print("Source Folder:", sourceFolder)
    print("Target Folder:", targetFolder)
    inStory = read_file_store(os.path.join(sourceFolder, sourceFile))
    inChoicescript_Stats = read_file_store(os.path.join(sourceFolder, "choicescript_stats.txt"))
    inChoicescript_startup = read_file_store(os.path.join(sourceFolder, "startup.txt"))    
    outStory = FileStore(os.path.join(targetFolder, targetFile))   

    csWriterConfig = CSWriterConfig(targetFolder, outStory,
                                      move_file_store(inChoicescript_Stats, targetFolder),
                                      move_file_store(inChoicescript_startup, targetFolder)
    )
    
    # Process the input script
    scriptEngine = ScriptEngine(inStory)
    scriptEngine.process()

    csEngine = CSEngine(csWriterConfig, scriptEngine.getScript())
    csEngine.process()

    # Write the cs files 
    csWriterConfig.write_all()

    print


