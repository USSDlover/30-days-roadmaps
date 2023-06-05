At this setup we are using vite and babylonjs.

There are some basic upkeep we'll have to keep in mind:
- You should occasionally run npm up (short for update) in the first terminal tab, which is the one for the main folder above your projects. This keeps Vite and Babylon.js updated.
- If you need to uninstall a package from Step 4 or otherwise, run npm un <packageNameHere> (short for uninstall) in that same main folder or terminal tab.
- Static assets such as images or 3D models should go in the public folder. These can then be referenced as if they're in the root folder "./likethis.png".
- If you ever get stuck, reach out to the Babylon forums for help.


## Building and sharing online

- Make sure all your non-code assets (images, 3D models, etc.) are in the public folder to ensure that they end up in the final bundle.
- If it's not already open as a tab, right-click on your project's folder (not the main one) and choose Open in Integrated Terminal. Or just click on your second Terminal tab if you still have it.
- Run this command: `npm run build`
- Your exported code bundle is now in a folder called `dist`. Check if it works by running: `npm run preview`
- **IMPORTANT**: Once you verify this test works, open `dist/index.html` and look for any file paths that point to root with `/`. Add a period in front of all of those root paths (meaning `/assets` would become `./assets`) and save the file.


## On setup note

Note to advanced users: The reason why we didn't just cd into the new folder is because it's convenient to have both the root and project folders open as separate tabs in our Terminal. Doing this lets us maintain our packages in the root folder separately from the project subfolder. We can install our necessary packages once in the root folder, and reference them freely in the code inside our project subfolders. NPM is smart enough to detect any packages installed in parent folders- you don't have to directly install them inside your project root directories. This is a good habit to get into instead of maintaining multiple copies of Vite and Babylon.js installed in every single project folder, resulting in wasted storage space. Feel free to deviate from this structure if you'd like, though.
