export interface RepoTemplate {
  id: string;
  name: string;
  description: string;
  files: {
    [path: string]: string;
  };
  gitignore?: string;
}

export const repoTemplates: RepoTemplate[] = [
  {
    id: 'node-typescript',
    name: 'Node.js + TypeScript',
    description: 'Modern Node.js project with TypeScript',
    files: {
      'package.json': JSON.stringify({
        name: 'project-name',
        version: '1.0.0',
        scripts: {
          build: 'tsc',
          start: 'node dist/index.js',
        },
        devDependencies: {
          typescript: '^5.0.0',
          '@types/node': '^20.0.0',
        },
      }, null, 2),
      'tsconfig.json': JSON.stringify({
        compilerOptions: {
          target: 'ES2020',
          module: 'commonjs',
          outDir: './dist',
          strict: true,
        },
      }, null, 2),
      'src/index.ts': 'console.log("Hello, World!");',
      'README.md': '# Project Name\n\nNode.js TypeScript project',
    },
    gitignore: 'node_modules/\ndist/\n*.log\n.env',
  },
  {
    id: 'react-app',
    name: 'React Application',
    description: 'React app with modern setup',
    files: {
      'package.json': JSON.stringify({
        name: 'react-app',
        version: '1.0.0',
        scripts: {
          start: 'react-scripts start',
          build: 'react-scripts build',
        },
        dependencies: {
          react: '^18.0.0',
          'react-dom': '^18.0.0',
        },
      }, null, 2),
      'public/index.html': '<!DOCTYPE html>\n<html>\n<head><title>React App</title></head>\n<body><div id="root"></div></body>\n</html>',
      'src/index.js': 'import React from "react";\nimport ReactDOM from "react-dom";\nimport App from "./App";\n\nReactDOM.render(<App />, document.getElementById("root"));',
      'src/App.js': 'import React from "react";\n\nfunction App() {\n  return <div>Hello React!</div>;\n}\n\nexport default App;',
      'README.md': '# React Application\n\nModern React app',
    },
    gitignore: 'node_modules/\nbuild/\n.DS_Store\n*.log',
  },
  {
    id: 'python-project',
    name: 'Python Project',
    description: 'Python project with standard structure',
    files: {
      'requirements.txt': '# Add your dependencies here\n',
      'main.py': 'def main():\n    print("Hello, Python!")\n\nif __name__ == "__main__":\n    main()',
      'README.md': '# Python Project\n\n## Setup\n```bash\npip install -r requirements.txt\npython main.py\n```',
    },
    gitignore: '__pycache__/\n*.py[cod]\n*$py.class\n.venv/\nvenv/\n.env',
  },
  {
    id: 'basic',
    name: 'Basic Repository',
    description: 'Simple repository with README',
    files: {
      'README.md': '# Project Name\n\nProject description goes here.',
      'LICENSE': 'MIT License\n\nCopyright (c) 2024\n\nPermission is hereby granted...',
    },
    gitignore: '.DS_Store\n*.log\n.env',
  },
];

export function getTemplate(id: string): RepoTemplate | undefined {
  return repoTemplates.find(t => t.id === id);
}

export function getAllTemplates(): RepoTemplate[] {
  return repoTemplates;
}
