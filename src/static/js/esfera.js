// Configuración de la escena, la cámara y el renderizador
const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
const renderer = new THREE.WebGLRenderer();
renderer.setSize(window.innerWidth, window.innerHeight);
document.body.appendChild(renderer.domElement);

// Crear una geometría de esfera
const geometry = new THREE.SphereGeometry(1, 32, 32);
const material = new THREE.MeshBasicMaterial({ color: 0x0077ff, wireframe: true });
const sphere = new THREE.Mesh(geometry, material);
scene.add(sphere);

// Posicionar la cámara
camera.position.z = 5;

// Función de animación para hacer girar la esfera
function animate() {
    requestAnimationFrame(animate);
    sphere.rotation.y += 0.01; // Rotación en el eje Y
    sphere.rotation.x += 0.005; // Rotación en el eje X
    renderer.render(scene, camera);
}

animate();

// Ajustar el renderizador al tamaño de la ventana si se cambia el tamaño
window.addEventListener('resize', () => {
    renderer.setSize(window.innerWidth, window.innerHeight);
    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectionMatrix();
});