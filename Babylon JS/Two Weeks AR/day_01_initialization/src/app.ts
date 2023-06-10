import "@babylonjs/core/Debug/debugLayer";
import "@babylonjs/inspector";
import { Engine, Scene, Vector3, HemisphericLight, MeshBuilder, FreeCamera } from '@babylonjs/core';

class App {
    constructor() {
        this.createScene();
    }

    async createScene() {
        // create the canvas html element and attach it to the webpage
        const canvas = document.createElement("canvas");
        canvas.style.width = "100%";
        canvas.style.height = "100%";
        canvas.id = "gameCanvas";
        document.body.appendChild(canvas);

        const engine = new Engine(canvas, true);
        const scene = new Scene(engine);

        const camera = new FreeCamera('camera1', new Vector3(0, 5, -10), scene);
        camera.setTarget(Vector3.Zero());
        camera.attachControl(canvas, true);

        const light = new HemisphericLight('light1', new Vector3(0, 1, 0), scene);
        light.intensity = 0.7;

        const sphere = MeshBuilder.CreateSphere('sphere1', { segments: 16, diameter: 2 }, scene);
        sphere.position.y = 1;

        scene.createDefaultEnvironment();

        await scene.createDefaultXRExperienceAsync({
            uiOptions: { sessionMode: 'immersive-ar' },
            optionalFeatures: true
        });

        engine.runRenderLoop(() => {
            scene.render();
        });
    }
}

new App();
