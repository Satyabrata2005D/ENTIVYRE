/**
 * ENTIVYRE — High-Dimensional 3D Vector Manifold Engine
 * Pure Canvas 3D renderer for high-dimensional entity resolution embedding space.
 * 100% offline, air-gapped, zero external dependencies.
 */

(function () {
  'use strict';

  // 32 High-Dimensional Entity Embeddings in Normalized 3D Coordinates [-150, 150]
  const VECTOR_ENTITIES = [
    // --- Cluster 01: Core Target (Acme Robotics) ---
    {
      id: 'S1-00001',
      name: 'Acme Robotics Inc.',
      category: 'anchor',
      cluster: 'CL-09412',
      source: 'Source 1 (Canonical)',
      address: '500 Market St, Suite 400, San Jose, CA 95113',
      phone: '+1 (408) 555-0192',
      umap: { x: 0, y: 15, z: 0 },
      pca: { x: 0, y: 10, z: 0 },
      tsne: { x: 0, y: 20, z: 0 },
      similarity: 1.000,
      classification: 'ANCHOR ENTITY',
      color: '#FF5B4D',
      radius: 9,
      features: { jaro: 1.0, token: 1.0, geo: 1.0, phone: 1.0 }
    },
    {
      id: 'S2-04812',
      name: 'Acme Robotics Incorporated',
      category: 'match',
      cluster: 'CL-09412',
      source: 'Source 2 (Partner Feed)',
      address: '500 Market Street #400, San Jose, CA 95113',
      phone: '+1 (408) 555-0192',
      umap: { x: 22, y: 32, z: -18 },
      pca: { x: 28, y: 25, z: -15 },
      tsne: { x: 20, y: 35, z: -25 },
      similarity: 0.974,
      classification: 'CONFIRMED MATCH',
      color: '#159A72',
      radius: 7,
      features: { jaro: 0.968, token: 0.932, geo: 0.995, phone: 1.0 }
    },
    {
      id: 'S3-11942',
      name: 'Acme Robotics, Corp.',
      category: 'match',
      cluster: 'CL-09412',
      source: 'Source 3 (Registry TSV)',
      address: '500 Market St Ste 400, San Jose, CA 95113',
      phone: '+1 (408) 555-0199',
      umap: { x: -28, y: 20, z: 24 },
      pca: { x: -22, y: 30, z: 20 },
      tsne: { x: -32, y: 18, z: 28 },
      similarity: 0.942,
      classification: 'CONFIRMED MATCH',
      color: '#159A72',
      radius: 7,
      features: { jaro: 0.935, token: 0.890, geo: 0.991, phone: 0.92 }
    },
    {
      id: 'S2-78602',
      name: 'Acme Robotics Technologies Inc',
      category: 'match',
      cluster: 'CL-09412',
      source: 'Source 2 (Partner Feed)',
      address: '502 Market St, Fl 4, San Jose, CA 95113',
      phone: '+1 (408) 555-0192',
      umap: { x: 15, y: -25, z: 30 },
      pca: { x: 18, y: -20, z: 26 },
      tsne: { x: 12, y: -30, z: 35 },
      similarity: 0.915,
      classification: 'CONFIRMED MATCH',
      color: '#159A72',
      radius: 6.5,
      features: { jaro: 0.902, token: 0.875, geo: 0.985, phone: 1.0 }
    },
    {
      id: 'S3-62588',
      name: 'Acme Robotics Lab LLC',
      category: 'match',
      cluster: 'CL-09412',
      source: 'Source 3 (Registry TSV)',
      address: '500 Market St, Bldg B, San Jose, CA 95113',
      phone: '+1 (408) 555-0145',
      umap: { x: -35, y: -18, z: -22 },
      pca: { x: -30, y: -15, z: -25 },
      tsne: { x: -40, y: -15, z: -18 },
      similarity: 0.898,
      classification: 'CONFIRMED MATCH',
      color: '#159A72',
      radius: 6,
      features: { jaro: 0.884, token: 0.860, geo: 0.990, phone: 0.85 }
    },
    {
      id: 'S2-43526',
      name: 'Acme Robotics Systems',
      category: 'match',
      cluster: 'CL-09412',
      source: 'Source 2 (Partner Feed)',
      address: '1100 Innovation Way, Sunnyvale, CA 94089',
      phone: '+1 (408) 732-9011',
      umap: { x: 42, y: 8, z: 38 },
      pca: { x: 45, y: 12, z: 32 },
      tsne: { x: 38, y: 10, z: 45 },
      similarity: 0.884,
      classification: 'CONFIRMED MATCH',
      color: '#159A72',
      radius: 6,
      features: { jaro: 0.871, token: 0.852, geo: 0.920, phone: 0.78 }
    },

    // --- Hard Negative Collisions / Look-Alikes (Repelled in Vector Space) ---
    {
      id: 'S2-99014',
      name: 'Acme Bakery LLC',
      category: 'collision',
      cluster: 'REJECTED',
      source: 'Source 2 (Partner Feed)',
      address: '124 5th Ave, New York, NY 10011',
      phone: '+1 (212) 555-8910',
      umap: { x: 135, y: 80, z: 90 },
      pca: { x: 140, y: 75, z: 85 },
      tsne: { x: 150, y: 85, z: 95 },
      similarity: 0.218,
      classification: 'REJECTED (COLLISION)',
      color: '#EF4444',
      radius: 6,
      features: { jaro: 0.420, token: 0.150, geo: 0.040, phone: 0.05 }
    },
    {
      id: 'S3-40118',
      name: 'Acme Hardware & Tools Supply',
      category: 'collision',
      cluster: 'REJECTED',
      source: 'Source 3 (Registry TSV)',
      address: '884 Industrial Blvd, Dallas, TX 75207',
      phone: '+1 (214) 555-4301',
      umap: { x: -120, y: 110, z: -85 },
      pca: { x: -125, y: 100, z: -90 },
      tsne: { x: -130, y: 120, z: -80 },
      similarity: 0.185,
      classification: 'REJECTED (COLLISION)',
      color: '#EF4444',
      radius: 5.5,
      features: { jaro: 0.380, token: 0.110, geo: 0.060, phone: 0.02 }
    },
    {
      id: 'S2-55102',
      name: 'Robotics Acme Solutions Corp',
      category: 'collision',
      cluster: 'REJECTED',
      source: 'Source 2 (Partner Feed)',
      address: '400 N Michigan Ave, Chicago, IL 60611',
      phone: '+1 (312) 555-7720',
      umap: { x: 95, y: -105, z: -110 },
      pca: { x: 100, y: -95, z: -115 },
      tsne: { x: 90, y: -115, z: -100 },
      similarity: 0.340,
      classification: 'REJECTED (COLLISION)',
      color: '#EF4444',
      radius: 5.5,
      features: { jaro: 0.580, token: 0.380, geo: 0.080, phone: 0.10 }
    },

    // --- Cluster 02: Apex Autonomous Labs (Neighboring Manifold) ---
    {
      id: 'S1-10640',
      name: 'Apex Autonomous Labs',
      category: 'ambient',
      cluster: 'CL-04182',
      source: 'Source 1 (Canonical)',
      address: '2300 Hanover St, Palo Alto, CA 94304',
      phone: '+1 (650) 843-1100',
      umap: { x: -90, y: -45, z: 75 },
      pca: { x: -85, y: -40, z: 70 },
      tsne: { x: -95, y: -50, z: 80 },
      similarity: 0.412,
      classification: 'AMBIENT MANIFOLD',
      color: '#4F46C5',
      radius: 6,
      features: { jaro: 0.32, token: 0.44, geo: 0.88, phone: 0.12 }
    },
    {
      id: 'S2-32150',
      name: 'Apex Autonomous Inc.',
      category: 'ambient',
      cluster: 'CL-04182',
      source: 'Source 2 (Partner Feed)',
      address: '2300 Hanover Street, Palo Alto, CA 94304',
      phone: '+1 (650) 843-1100',
      umap: { x: -105, y: -38, z: 62 },
      pca: { x: -100, y: -35, z: 58 },
      tsne: { x: -110, y: -42, z: 68 },
      similarity: 0.395,
      classification: 'AMBIENT MANIFOLD',
      color: '#4F46C5',
      radius: 5.5,
      features: { jaro: 0.31, token: 0.42, geo: 0.88, phone: 0.12 }
    },
    {
      id: 'S3-90889',
      name: 'Apex Auto AI Group',
      category: 'ambient',
      cluster: 'CL-04182',
      source: 'Source 3 (Registry TSV)',
      address: '400 Castro St, Mountain View, CA 94041',
      phone: '+1 (650) 961-4422',
      umap: { x: -75, y: -60, z: 88 },
      pca: { x: -70, y: -55, z: 82 },
      tsne: { x: -80, y: -65, z: 92 },
      similarity: 0.380,
      classification: 'AMBIENT MANIFOLD',
      color: '#4F46C5',
      radius: 5,
      features: { jaro: 0.28, token: 0.39, geo: 0.82, phone: 0.10 }
    },

    // --- Cluster 03: Cognitive Bots (San Francisco Manifold) ---
    {
      id: 'S1-15628',
      name: 'Cognitive Bots Corporation',
      category: 'ambient',
      cluster: 'CL-01198',
      source: 'Source 1 (Canonical)',
      address: '100 Montgomery St, Suite 1800, San Francisco, CA 94104',
      phone: '+1 (415) 392-8000',
      umap: { x: 75, y: 110, z: -60 },
      pca: { x: 70, y: 105, z: -55 },
      tsne: { x: 80, y: 115, z: -65 },
      similarity: 0.425,
      classification: 'AMBIENT MANIFOLD',
      color: '#06B6D4',
      radius: 6,
      features: { jaro: 0.35, token: 0.41, geo: 0.74, phone: 0.08 }
    },
    {
      id: 'S2-53024',
      name: 'Cognitive Bots LLC',
      category: 'ambient',
      cluster: 'CL-01198',
      source: 'Source 2 (Partner Feed)',
      address: '100 Montgomery St #1800, San Francisco, CA 94104',
      phone: '+1 (415) 392-8000',
      umap: { x: 62, y: 122, z: -75 },
      pca: { x: 58, y: 118, z: -70 },
      tsne: { x: 68, y: 126, z: -80 },
      similarity: 0.410,
      classification: 'AMBIENT MANIFOLD',
      color: '#06B6D4',
      radius: 5.5,
      features: { jaro: 0.34, token: 0.40, geo: 0.74, phone: 0.08 }
    },
    {
      id: 'S3-33379',
      name: 'Cognitive Robotics Group',
      category: 'ambient',
      cluster: 'CL-01198',
      source: 'Source 3 (Registry TSV)',
      address: '1999 Harrison St, Oakland, CA 94612',
      phone: '+1 (510) 834-2200',
      umap: { x: 90, y: 95, z: -48 },
      pca: { x: 85, y: 90, z: -45 },
      tsne: { x: 95, y: 100, z: -52 },
      similarity: 0.402,
      classification: 'AMBIENT MANIFOLD',
      color: '#06B6D4',
      radius: 5,
      features: { jaro: 0.38, token: 0.39, geo: 0.71, phone: 0.06 }
    },

    // --- Cluster 04: Kinetic Dynamics (Austin TX Manifold) ---
    {
      id: 'S1-68982',
      name: 'Kinetic Dynamics Inc.',
      category: 'ambient',
      cluster: 'CL-08819',
      source: 'Source 1 (Canonical)',
      address: '701 Brazos St, Austin, TX 78701',
      phone: '+1 (512) 474-1200',
      umap: { x: -110, y: 40, z: -120 },
      pca: { x: -105, y: 45, z: -115 },
      tsne: { x: -115, y: 35, z: -125 },
      similarity: 0.310,
      classification: 'AMBIENT MANIFOLD',
      color: '#EC4899',
      radius: 6,
      features: { jaro: 0.28, token: 0.32, geo: 0.12, phone: 0.04 }
    },
    {
      id: 'S2-98930',
      name: 'Kinetic Dynamics LLC',
      category: 'ambient',
      cluster: 'CL-08819',
      source: 'Source 2 (Partner Feed)',
      address: '701 Brazos St, Suite 400, Austin, TX 78701',
      phone: '+1 (512) 474-1200',
      umap: { x: -125, y: 52, z: -105 },
      pca: { x: -120, y: 56, z: -100 },
      tsne: { x: -130, y: 48, z: -110 },
      similarity: 0.298,
      classification: 'AMBIENT MANIFOLD',
      color: '#EC4899',
      radius: 5.5,
      features: { jaro: 0.27, token: 0.31, geo: 0.12, phone: 0.04 }
    },
    {
      id: 'S3-50645',
      name: 'Kinetic Dynamics Technologies',
      category: 'ambient',
      cluster: 'CL-08819',
      source: 'Source 3 (Registry TSV)',
      address: '100 Congress Ave, Austin, TX 78701',
      phone: '+1 (512) 617-8900',
      umap: { x: -95, y: 28, z: -135 },
      pca: { x: -90, y: 32, z: -130 },
      tsne: { x: -100, y: 24, z: -140 },
      similarity: 0.285,
      classification: 'AMBIENT MANIFOLD',
      color: '#EC4899',
      radius: 5,
      features: { jaro: 0.25, token: 0.29, geo: 0.12, phone: 0.03 }
    }
  ];

  // Dynamic pairwise similarity edges to render in 3D
  const VECTOR_EDGES = [
    // Core Cluster edges to Anchor
    { sourceId: 'S1-00001', targetId: 'S2-04812', weight: 0.974, type: 'match' },
    { sourceId: 'S1-00001', targetId: 'S3-11942', weight: 0.942, type: 'match' },
    { sourceId: 'S1-00001', targetId: 'S2-78602', weight: 0.915, type: 'match' },
    { sourceId: 'S1-00001', targetId: 'S3-62588', weight: 0.898, type: 'match' },
    { sourceId: 'S1-00001', targetId: 'S2-43526', weight: 0.884, type: 'match' },
    // Cross-transitive closure edges within match cluster
    { sourceId: 'S2-04812', targetId: 'S3-11942', weight: 0.965, type: 'transitive' },
    { sourceId: 'S2-04812', targetId: 'S2-78602', weight: 0.928, type: 'transitive' },
    { sourceId: 'S3-11942', targetId: 'S3-62588', weight: 0.910, type: 'transitive' },
    // Collision repulsion vectors
    { sourceId: 'S1-00001', targetId: 'S2-99014', weight: 0.218, type: 'collision' },
    { sourceId: 'S1-00001', targetId: 'S3-40118', weight: 0.185, type: 'collision' },
    { sourceId: 'S1-00001', targetId: 'S2-55102', weight: 0.340, type: 'collision' },
    // Ambient cluster internal edges
    { sourceId: 'S1-10640', targetId: 'S2-32150', weight: 0.985, type: 'ambient' },
    { sourceId: 'S1-10640', targetId: 'S3-90889', weight: 0.940, type: 'ambient' },
    { sourceId: 'S1-15628', targetId: 'S2-53024', weight: 0.990, type: 'ambient' },
    { sourceId: 'S1-15628', targetId: 'S3-33379', weight: 0.935, type: 'ambient' },
    { sourceId: 'S1-68982', targetId: 'S2-98930', weight: 0.988, type: 'ambient' },
    { sourceId: 'S1-68982', targetId: 'S3-50645', weight: 0.922, type: 'ambient' }
  ];

  // Ambient 3D floating dust / star particles
  const BACKGROUND_STARS = [];
  for (let i = 0; i < 90; i++) {
    BACKGROUND_STARS.push({
      x: (Math.random() - 0.5) * 500,
      y: (Math.random() - 0.5) * 500,
      z: (Math.random() - 0.5) * 500,
      size: Math.random() * 1.5 + 0.5,
      alpha: Math.random() * 0.4 + 0.1
    });
  }

  // 3D Engine State
  const state = {
    isOpen: false,
    projectionMode: 'umap', // 'umap', 'pca', 'tsne'
    morphProgress: 1.0,
    morphStart: null,
    morphDuration: 800,
    currentCoords: {}, // id -> {x, y, z}
    targetCoords: {},

    // Camera
    cameraDistance: 420,
    minDistance: 160,
    maxDistance: 900,
    rotX: 0.38, // Pitch
    rotY: -0.65, // Yaw
    targetRotX: 0.38,
    targetRotY: -0.65,
    panX: 0,
    panY: 0,
    targetPanX: 0,
    targetPanY: 0,
    autoRotate: true,
    autoRotateSpeed: 0.003,
    showGrid: true,
    showLabels: true,

    // Interaction
    isDragging: false,
    dragButton: 0, // 0 = left, 2 = right
    lastMouseX: 0,
    lastMouseY: 0,
    hoveredNode: null,
    selectedNode: null,
    mouseX: 0,
    mouseY: 0,

    // Animation
    pulsePhase: 0,
    animFrameId: null,
    dpr: window.devicePixelRatio || 1
  };

  // DOM Elements
  let modalElem = null;
  let canvasElem = null;
  let ctx = null;
  let tooltipElem = null;
  let searchInput = null;

  // Initialize on DOM ready
  document.addEventListener('DOMContentLoaded', () => {
    initEngine();
  });

  function initEngine() {
    modalElem = document.getElementById('vector3dModal');
    canvasElem = document.getElementById('vector3dCanvas');
    if (!canvasElem || !modalElem) return;

    ctx = canvasElem.getContext('2d');
    tooltipElem = document.getElementById('vector3dTooltip');
    searchInput = document.getElementById('v3dSearchInput');

    // Initialize current & target coordinates
    VECTOR_ENTITIES.forEach(n => {
      state.currentCoords[n.id] = { ...n.umap };
      state.targetCoords[n.id] = { ...n.umap };
    });

    // Default select Anchor node
    state.selectedNode = VECTOR_ENTITIES[0];

    setupEventListeners();
    populateEntityList();
  }

  function setupEventListeners() {
    // Window Resize
    window.addEventListener('resize', () => {
      if (state.isOpen) resizeCanvas();
    });

    // Open button triggers
    document.querySelectorAll('.btn-open-3d-vector, [data-trigger="open-3d-vector"]').forEach(btn => {
      btn.addEventListener('click', (e) => {
        e.preventDefault();
        openVector3DModal();
      });
    });

    // Close button
    const btnClose = document.getElementById('btnVector3dClose');
    if (btnClose) {
      btnClose.addEventListener('click', closeVector3DModal);
    }

    // Fullscreen toggle
    const btnFullscreen = document.getElementById('btnVector3dFullscreen');
    if (btnFullscreen) {
      btnFullscreen.addEventListener('click', toggleNativeFullscreen);
    }

    // Reset Camera
    const btnResetCam = document.getElementById('btnVector3dResetCam');
    if (btnResetCam) {
      btnResetCam.addEventListener('click', resetCamera);
    }

    // Auto-Rotate Toggle
    const btnAutoRotate = document.getElementById('btnVector3dAutoRotate');
    if (btnAutoRotate) {
      btnAutoRotate.addEventListener('click', () => {
        state.autoRotate = !state.autoRotate;
        btnAutoRotate.classList.toggle('active', state.autoRotate);
        const icon = btnAutoRotate.querySelector('.auto-rotate-indicator');
        if (icon) icon.innerText = state.autoRotate ? 'ON' : 'OFF';
      });
    }

    // Projection Mode Buttons (UMAP / PCA / t-SNE)
    document.querySelectorAll('.proj-mode-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        const mode = btn.getAttribute('data-mode');
        switchProjectionMode(mode);
      });
    });

    // Toggle Grid
    const btnToggleGrid = document.getElementById('btnVector3dGrid');
    if (btnToggleGrid) {
      btnToggleGrid.addEventListener('click', () => {
        state.showGrid = !state.showGrid;
        btnToggleGrid.classList.toggle('active', state.showGrid);
      });
    }

    // Canvas Mouse Interactions
    canvasElem.addEventListener('mousedown', onMouseDown);
    window.addEventListener('mousemove', onMouseMove);
    window.addEventListener('mouseup', onMouseUp);
    canvasElem.addEventListener('wheel', onWheel, { passive: false });
    canvasElem.addEventListener('contextmenu', e => e.preventDefault());

    // Canvas Touch Interactions for trackpads / touch devices
    canvasElem.addEventListener('touchstart', onTouchStart, { passive: false });
    canvasElem.addEventListener('touchmove', onTouchMove, { passive: false });
    canvasElem.addEventListener('touchend', onTouchEnd);

    // Search filter
    if (searchInput) {
      searchInput.addEventListener('input', (e) => {
        const query = e.target.value.toLowerCase().trim();
        filterEntityList(query);
      });
    }

    // Keyboard Shortcuts (Esc to close, Space to toggle rotate, R to reset camera)
    window.addEventListener('keydown', (e) => {
      if (!state.isOpen) return;
      if (e.key === 'Escape') {
        closeVector3DModal();
      } else if (e.key === ' ' && document.activeElement !== searchInput) {
        e.preventDefault();
        state.autoRotate = !state.autoRotate;
        const btn = document.getElementById('btnVector3dAutoRotate');
        if (btn) btn.classList.toggle('active', state.autoRotate);
      } else if ((e.key === 'r' || e.key === 'R') && document.activeElement !== searchInput) {
        resetCamera();
      }
    });
  }

  // --- Public Modal Controls ---
  window.openVector3DModal = function (anchorId, pairId) {
    if (!modalElem) modalElem = document.getElementById('vector3dModal');
    if (!modalElem) return;

    modalElem.classList.add('open');
    document.body.style.overflow = 'hidden';
    state.isOpen = true;

    resizeCanvas();
    resetCamera();

    // If specific pair was selected, highlight it
    if (pairId) {
      const match = VECTOR_ENTITIES.find(e => e.id === pairId);
      if (match) selectNode(match);
    } else {
      selectNode(VECTOR_ENTITIES[0]);
    }

    // Start 60fps render loop
    if (!state.animFrameId) {
      state.animFrameId = requestAnimationFrame(renderLoop);
    }

    if (window.showToast) {
      window.showToast('🚀 High-Dimensional 3D Vector Manifold initialized in Fullscreen');
    }
  };

  window.closeVector3DModal = function () {
    if (!modalElem) return;
    modalElem.classList.remove('open');
    document.body.style.overflow = '';
    state.isOpen = false;

    if (document.fullscreenElement) {
      document.exitFullscreen().catch(() => {});
    }

    if (state.animFrameId) {
      cancelAnimationFrame(state.animFrameId);
      state.animFrameId = null;
    }
  };

  function toggleNativeFullscreen() {
    if (!document.fullscreenElement) {
      modalElem.requestFullscreen().catch(err => {
        console.warn('Native fullscreen request blocked:', err);
      });
    } else {
      document.exitFullscreen().catch(() => {});
    }
  }

  function resizeCanvas() {
    if (!canvasElem) return;
    const rect = canvasElem.getBoundingClientRect();
    const width = rect.width || window.innerWidth;
    const height = rect.height || window.innerHeight;

    state.dpr = window.devicePixelRatio || 1;
    canvasElem.width = width * state.dpr;
    canvasElem.height = height * state.dpr;
    ctx.scale(state.dpr, state.dpr);
  }

  function resetCamera() {
    state.targetRotX = 0.38;
    state.targetRotY = -0.65;
    state.targetDistance = 420;
    state.cameraDistance = 420;
    state.targetPanX = 0;
    state.targetPanY = 0;
    state.panX = 0;
    state.panY = 0;
  }

  function switchProjectionMode(newMode) {
    if (newMode === state.projectionMode) return;
    state.projectionMode = newMode;

    document.querySelectorAll('.proj-mode-btn').forEach(btn => {
      btn.classList.toggle('active', btn.getAttribute('data-mode') === newMode);
    });

    const modeTag = document.getElementById('v3dActiveModeTag');
    if (modeTag) modeTag.innerText = newMode.toUpperCase() + ' 3D';

    // Set target coordinates for smooth morph
    VECTOR_ENTITIES.forEach(n => {
      state.targetCoords[n.id] = { ...n[newMode] };
    });

    state.morphProgress = 0;
    state.morphStart = performance.now();

    if (window.showToast) {
      window.showToast(`Morphing vector manifold to ${newMode.toUpperCase()} 3D projection...`);
    }
  }

  // --- Mouse / Touch Handlers ---
  function onMouseDown(e) {
    state.isDragging = true;
    state.dragButton = e.button;
    state.lastMouseX = e.clientX;
    state.lastMouseY = e.clientY;
  }

  function onMouseMove(e) {
    const rect = canvasElem.getBoundingClientRect();
    state.mouseX = e.clientX - rect.left;
    state.mouseY = e.clientY - rect.top;

    if (state.isDragging) {
      const deltaX = e.clientX - state.lastMouseX;
      const deltaY = e.clientY - state.lastMouseY;

      if (state.dragButton === 0 && !e.shiftKey) {
        // Orbit rotation
        state.targetRotY += deltaX * 0.007;
        state.targetRotX += deltaY * 0.007;
        // Clamp pitch to prevent flipping upside down
        state.targetRotX = Math.max(-Math.PI / 2.2, Math.min(Math.PI / 2.2, state.targetRotX));
      } else {
        // Pan
        state.targetPanX += deltaX * 0.45;
        state.targetPanY += deltaY * 0.45;
      }

      state.lastMouseX = e.clientX;
      state.lastMouseY = e.clientY;
    } else {
      // Raycasting / Hit-testing on hover
      checkNodeHover(state.mouseX, state.mouseY);
    }
  }

  function onMouseUp(e) {
    if (state.isDragging) {
      state.isDragging = false;
      // If mouse barely moved, treat as click selection
      const delta = Math.hypot(e.clientX - state.lastMouseX, e.clientY - state.lastMouseY);
      if (delta < 5 && state.hoveredNode) {
        selectNode(state.hoveredNode);
      }
    }
  }

  function onWheel(e) {
    e.preventDefault();
    const zoomFactor = e.deltaY > 0 ? 1.08 : 0.92;
    state.cameraDistance = Math.max(state.minDistance, Math.min(state.maxDistance, state.cameraDistance * zoomFactor));
  }

  let touchStartDist = 0;
  function onTouchStart(e) {
    if (e.touches.length === 1) {
      state.isDragging = true;
      state.lastMouseX = e.touches[0].clientX;
      state.lastMouseY = e.touches[0].clientY;
    } else if (e.touches.length === 2) {
      touchStartDist = Math.hypot(
        e.touches[0].clientX - e.touches[1].clientX,
        e.touches[0].clientY - e.touches[1].clientY
      );
    }
  }

  function onTouchMove(e) {
    e.preventDefault();
    if (e.touches.length === 1 && state.isDragging) {
      const deltaX = e.touches[0].clientX - state.lastMouseX;
      const deltaY = e.touches[0].clientY - state.lastMouseY;
      state.targetRotY += deltaX * 0.007;
      state.targetRotX += deltaY * 0.007;
      state.lastMouseX = e.touches[0].clientX;
      state.lastMouseY = e.touches[0].clientY;
    } else if (e.touches.length === 2) {
      const dist = Math.hypot(
        e.touches[0].clientX - e.touches[1].clientX,
        e.touches[0].clientY - e.touches[1].clientY
      );
      const zoomFactor = touchStartDist / dist;
      state.cameraDistance = Math.max(state.minDistance, Math.min(state.maxDistance, state.cameraDistance * (zoomFactor > 1 ? 1.03 : 0.97)));
      touchStartDist = dist;
    }
  }

  function onTouchEnd() {
    state.isDragging = false;
  }

  // --- 3D Projection Math ---
  function project3D(x, y, z, width, height) {
    // 1. Rotate Y (Yaw)
    const cosY = Math.cos(state.rotY);
    const sinY = Math.sin(state.rotY);
    const x1 = x * cosY - z * sinY;
    const z1 = z * cosY + x * sinY;

    // 2. Rotate X (Pitch)
    const cosX = Math.cos(state.rotX);
    const sinX = Math.sin(state.rotX);
    const y2 = y * cosX - z1 * sinX;
    const z2 = z1 * cosX + y * sinX;

    // 3. Perspective Projection
    const fov = 500;
    const distance = state.cameraDistance + z2;
    if (distance <= 10) return null; // Behind camera

    const scale = fov / distance;
    const screenX = (x1 * scale) + (width / 2) + state.panX;
    const screenY = (-y2 * scale) + (height / 2) + state.panY;

    return {
      x: screenX,
      y: screenY,
      scale: scale,
      depth: z2
    };
  }

  // --- Render Loop (60 FPS) ---
  function renderLoop(timestamp) {
    if (!state.isOpen) return;

    const width = canvasElem.width / state.dpr;
    const height = canvasElem.height / state.dpr;

    // Smooth camera damping
    state.rotX += (state.targetRotX - state.rotX) * 0.08;
    state.rotY += (state.targetRotY - state.rotY) * 0.08;
    state.panX += (state.targetPanX - state.panX) * 0.08;
    state.panY += (state.targetPanY - state.panY) * 0.08;

    // Auto rotate when idle
    if (state.autoRotate && !state.isDragging) {
      state.targetRotY += state.autoRotateSpeed;
      state.rotY += state.autoRotateSpeed;
    }

    // Morph coordinates animation
    if (state.morphProgress < 1.0 && state.morphStart) {
      const elapsed = timestamp - state.morphStart;
      state.morphProgress = Math.min(1.0, elapsed / state.morphDuration);
      const ease = 0.5 - Math.cos(state.morphProgress * Math.PI) / 2; // Smooth cosine ease

      VECTOR_ENTITIES.forEach(n => {
        const cur = state.currentCoords[n.id];
        const tgt = state.targetCoords[n.id];
        cur.x += (tgt.x - cur.x) * ease * 0.2;
        cur.y += (tgt.y - cur.y) * ease * 0.2;
        cur.z += (tgt.z - cur.z) * ease * 0.2;
      });
    }

    state.pulsePhase += 0.04;

    // Clear Screen with deep tech gradient
    ctx.clearRect(0, 0, width, height);

    // Render Ambient 3D Stars
    renderBackgroundStars(width, height);

    // Render 3D Coordinate Bounding Grid & Axes
    if (state.showGrid) {
      render3DGrid(width, height);
    }

    // Render Edges
    renderEdges(width, height);

    // Project and Sort Nodes by Depth (Painter's Algorithm)
    const projectedNodes = [];
    VECTOR_ENTITIES.forEach(entity => {
      const coords = state.currentCoords[entity.id];
      const proj = project3D(coords.x, coords.y, coords.z, width, height);
      if (proj) {
        projectedNodes.push({
          entity: entity,
          proj: proj,
          depth: proj.depth
        });
      }
    });

    // Sort far to near
    projectedNodes.sort((a, b) => b.depth - a.depth);

    // Render Nodes
    projectedNodes.forEach(item => {
      renderNode(item.entity, item.proj);
    });

    state.animFrameId = requestAnimationFrame(renderLoop);
  }

  function renderBackgroundStars(width, height) {
    ctx.save();
    BACKGROUND_STARS.forEach(s => {
      const proj = project3D(s.x, s.y, s.z, width, height);
      if (proj && proj.scale > 0) {
        ctx.fillStyle = `rgba(180, 195, 230, ${s.alpha * Math.min(1, proj.scale * 1.2)})`;
        ctx.beginPath();
        ctx.arc(proj.x, proj.y, s.size * proj.scale, 0, Math.PI * 2);
        ctx.fill();
      }
    });
    ctx.restore();
  }

  function render3DGrid(width, height) {
    ctx.save();
    const boxSize = 160;
    const yFloor = -110;

    // Floor Grid lines on X-Z plane
    ctx.strokeStyle = 'rgba(79, 70, 197, 0.12)';
    ctx.lineWidth = 1;

    for (let i = -boxSize; i <= boxSize; i += 40) {
      // Lines parallel to Z
      const p1 = project3D(i, yFloor, -boxSize, width, height);
      const p2 = project3D(i, yFloor, boxSize, width, height);
      if (p1 && p2) {
        ctx.beginPath();
        ctx.moveTo(p1.x, p1.y);
        ctx.lineTo(p2.x, p2.y);
        ctx.stroke();
      }

      // Lines parallel to X
      const p3 = project3D(-boxSize, yFloor, i, width, height);
      const p4 = project3D(boxSize, yFloor, i, width, height);
      if (p3 && p4) {
        ctx.beginPath();
        ctx.moveTo(p3.x, p3.y);
        ctx.lineTo(p4.x, p4.y);
        ctx.stroke();
      }
    }

    // 3D Principal Axes (Origin at 0, 0, 0)
    const o = project3D(0, 0, 0, width, height);
    const axX = project3D(70, 0, 0, width, height);
    const axY = project3D(0, 70, 0, width, height);
    const axZ = project3D(0, 0, 70, width, height);

    if (o) {
      // X Axis (Red)
      if (axX) {
        ctx.strokeStyle = 'rgba(255, 91, 77, 0.6)';
        ctx.lineWidth = 1.5;
        ctx.beginPath();
        ctx.moveTo(o.x, o.y);
        ctx.lineTo(axX.x, axX.y);
        ctx.stroke();
        ctx.fillStyle = '#FF5B4D';
        ctx.font = '9px monospace';
        ctx.fillText('+Dim X', axX.x + 4, axX.y + 3);
      }
      // Y Axis (Green)
      if (axY) {
        ctx.strokeStyle = 'rgba(21, 154, 114, 0.6)';
        ctx.lineWidth = 1.5;
        ctx.beginPath();
        ctx.moveTo(o.x, o.y);
        ctx.lineTo(axY.x, axY.y);
        ctx.stroke();
        ctx.fillStyle = '#159A72';
        ctx.font = '9px monospace';
        ctx.fillText('+Dim Y', axY.x + 4, axY.y - 4);
      }
      // Z Axis (Blue)
      if (axZ) {
        ctx.strokeStyle = 'rgba(79, 70, 197, 0.6)';
        ctx.lineWidth = 1.5;
        ctx.beginPath();
        ctx.moveTo(o.x, o.y);
        ctx.lineTo(axZ.x, axZ.y);
        ctx.stroke();
        ctx.fillStyle = '#818CF8';
        ctx.font = '9px monospace';
        ctx.fillText('+Dim Z', axZ.x + 4, axZ.y + 4);
      }
    }

    ctx.restore();
  }

  function renderEdges(width, height) {
    ctx.save();

    VECTOR_EDGES.forEach(edge => {
      const src = state.currentCoords[edge.sourceId];
      const tgt = state.currentCoords[edge.targetId];
      if (!src || !tgt) return;

      const p1 = project3D(src.x, src.y, src.z, width, height);
      const p2 = project3D(tgt.x, tgt.y, tgt.z, width, height);
      if (!p1 || !p2) return;

      const isAnchorEdge = edge.sourceId === 'S1-00001' || edge.targetId === 'S1-00001';
      const isSelectedEdge = state.selectedNode && (edge.sourceId === state.selectedNode.id || edge.targetId === state.selectedNode.id);

      ctx.beginPath();
      ctx.moveTo(p1.x, p1.y);
      ctx.lineTo(p2.x, p2.y);

      if (edge.type === 'match') {
        ctx.strokeStyle = isSelectedEdge ? 'rgba(21, 154, 114, 0.85)' : 'rgba(21, 154, 114, 0.45)';
        ctx.lineWidth = (isSelectedEdge ? 2.2 : 1.4) * Math.min(p1.scale, p2.scale);
        ctx.setLineDash([4, 3]);
        ctx.lineDashOffset = -state.pulsePhase * 8;
      } else if (edge.type === 'collision') {
        ctx.strokeStyle = 'rgba(239, 68, 68, 0.35)';
        ctx.lineWidth = 1.0 * Math.min(p1.scale, p2.scale);
        ctx.setLineDash([2, 4]);
      } else if (edge.type === 'transitive') {
        ctx.strokeStyle = 'rgba(21, 154, 114, 0.25)';
        ctx.lineWidth = 0.8 * Math.min(p1.scale, p2.scale);
        ctx.setLineDash([]);
      } else {
        ctx.strokeStyle = 'rgba(79, 70, 197, 0.2)';
        ctx.lineWidth = 0.7 * Math.min(p1.scale, p2.scale);
        ctx.setLineDash([]);
      }

      ctx.stroke();
    });

    ctx.restore();
  }

  function renderNode(entity, proj) {
    const isAnchor = entity.category === 'anchor';
    const isSelected = state.selectedNode && state.selectedNode.id === entity.id;
    const isHovered = state.hoveredNode && state.hoveredNode.id === entity.id;

    const baseRadius = entity.radius || 6;
    const radius = Math.max(3, baseRadius * proj.scale * (isSelected ? 1.3 : isHovered ? 1.2 : 1.0));

    ctx.save();

    // Pulsing Outer Rings for Anchor Node
    if (isAnchor) {
      const pulseSize = radius + 6 + Math.sin(state.pulsePhase) * 3;
      ctx.beginPath();
      ctx.arc(proj.x, proj.y, pulseSize, 0, Math.PI * 2);
      ctx.strokeStyle = 'rgba(255, 91, 77, 0.35)';
      ctx.lineWidth = 1.5;
      ctx.stroke();

      const pulseSize2 = radius + 12 + Math.sin(state.pulsePhase + 1) * 4;
      ctx.beginPath();
      ctx.arc(proj.x, proj.y, pulseSize2, 0, Math.PI * 2);
      ctx.strokeStyle = 'rgba(255, 91, 77, 0.15)';
      ctx.lineWidth = 1;
      ctx.stroke();
    }

    // Selection Halo
    if (isSelected) {
      ctx.beginPath();
      ctx.arc(proj.x, proj.y, radius + 5, 0, Math.PI * 2);
      ctx.strokeStyle = '#FFFFFF';
      ctx.lineWidth = 2;
      ctx.shadowColor = entity.color;
      ctx.shadowBlur = 12;
      ctx.stroke();
    } else if (isHovered) {
      ctx.beginPath();
      ctx.arc(proj.x, proj.y, radius + 4, 0, Math.PI * 2);
      ctx.strokeStyle = 'rgba(255, 255, 255, 0.6)';
      ctx.lineWidth = 1.5;
      ctx.stroke();
    }

    // Glowing Node Body (Radial Gradient for 3D Sphere Look)
    const grad = ctx.createRadialGradient(
      proj.x - radius * 0.3,
      proj.y - radius * 0.3,
      radius * 0.1,
      proj.x,
      proj.y,
      radius
    );

    if (isAnchor) {
      grad.addColorStop(0, '#FFA299');
      grad.addColorStop(0.7, '#FF5B4D');
      grad.addColorStop(1, '#B91C1C');
    } else if (entity.category === 'match') {
      grad.addColorStop(0, '#6EE7B7');
      grad.addColorStop(0.7, '#159A72');
      grad.addColorStop(1, '#065F46');
    } else if (entity.category === 'collision') {
      grad.addColorStop(0, '#FCA5A5');
      grad.addColorStop(0.7, '#EF4444');
      grad.addColorStop(1, '#7F1D1D');
    } else {
      grad.addColorStop(0, '#C7D2FE');
      grad.addColorStop(0.7, entity.color || '#4F46C5');
      grad.addColorStop(1, '#1E1B4B');
    }

    ctx.beginPath();
    ctx.arc(proj.x, proj.y, radius, 0, Math.PI * 2);
    ctx.fillStyle = grad;
    ctx.shadowColor = entity.color;
    ctx.shadowBlur = (isAnchor || isSelected || isHovered) ? 14 : 6;
    ctx.fill();

    // Node Label
    if (state.showLabels || isAnchor || isSelected || isHovered) {
      ctx.shadowBlur = 0;
      ctx.font = isAnchor ? 'bold 11px Inter, sans-serif' : '10px Inter, sans-serif';
      ctx.fillStyle = isSelected ? '#FFFFFF' : isAnchor ? '#FFB2A8' : 'rgba(230, 235, 245, 0.85)';
      ctx.textAlign = 'left';
      ctx.fillText(entity.name, proj.x + radius + 7, proj.y + 3);

      if (isAnchor || isSelected) {
        ctx.font = '9px monospace';
        ctx.fillStyle = isAnchor ? '#FF5B4D' : entity.color;
        ctx.fillText(`${entity.id} • ${entity.similarity ? (entity.similarity * 100).toFixed(1) + '%' : ''}`, proj.x + radius + 7, proj.y + 14);
      }
    }

    ctx.restore();
  }

  // --- Raycasting / Hit Testing ---
  function checkNodeHover(mouseX, mouseY) {
    const width = canvasElem.width / state.dpr;
    const height = canvasElem.height / state.dpr;

    let closest = null;
    let closestDist = 18; // Hit radius

    VECTOR_ENTITIES.forEach(entity => {
      const coords = state.currentCoords[entity.id];
      const proj = project3D(coords.x, coords.y, coords.z, width, height);
      if (proj) {
        const dist = Math.hypot(mouseX - proj.x, mouseY - proj.y);
        if (dist < closestDist) {
          closestDist = dist;
          closest = { entity, proj };
        }
      }
    });

    state.hoveredNode = closest ? closest.entity : null;

    if (closest) {
      canvasElem.style.cursor = 'pointer';
      show3DTooltip(closest.entity, closest.proj);
    } else {
      canvasElem.style.cursor = state.isDragging ? 'grabbing' : 'grab';
      hide3DTooltip();
    }
  }

  function show3DTooltip(entity, proj) {
    if (!tooltipElem) return;
    tooltipElem.innerHTML = `
      <div class="v3d-tt-header" style="color:${entity.color};">
        <span>${entity.id}</span>
        <span class="v3d-tt-sim">${(entity.similarity * 100).toFixed(1)}% Sim</span>
      </div>
      <div class="v3d-tt-name">${entity.name}</div>
      <div class="v3d-tt-sub">${entity.classification} &middot; ${entity.source}</div>
      <div class="v3d-tt-sub">${entity.address.split(',')[0]}</div>
    `;

    tooltipElem.style.left = `${proj.x + 16}px`;
    tooltipElem.style.top = `${proj.y - 12}px`;
    tooltipElem.classList.add('visible');
  }

  function hide3DTooltip() {
    if (tooltipElem) tooltipElem.classList.remove('visible');
  }

  // --- Selection and Inspector Panel ---
  function selectNode(entity) {
    state.selectedNode = entity;

    // Update Node Inspector Card
    const card = document.getElementById('v3dInspectorCard');
    if (!card) return;

    card.innerHTML = `
      <div class="v3d-inspect-header">
        <div>
          <span class="v3d-inspect-badge" style="background:${entity.color}22; color:${entity.color}; border:1px solid ${entity.color}44;">
            ${entity.classification}
          </span>
          <h4 class="v3d-inspect-title">${entity.name}</h4>
          <span class="v3d-inspect-id">${entity.id} &middot; ${entity.source}</span>
        </div>
      </div>

      <div class="v3d-inspect-grid">
        <div class="v3d-field-box">
          <span class="v3d-f-label">CLUSTER IDENTIFIER</span>
          <span class="v3d-f-val">${entity.cluster}</span>
        </div>
        <div class="v3d-field-box">
          <span class="v3d-f-label">COSINE SIMILARITY</span>
          <span class="v3d-f-val" style="color:${entity.color};">${(entity.similarity * 100).toFixed(1)}%</span>
        </div>
      </div>

      <div class="v3d-address-box">
        <span class="v3d-f-label">REGISTERED ADDRESS &amp; PHONE</span>
        <div class="v3d-addr-text">${entity.address}</div>
        <div class="v3d-addr-phone">${entity.phone}</div>
      </div>

      <div class="v3d-features-heading">High-Dimensional Feature Decomposition</div>

      <div class="v3d-feat-row">
        <span>Jaro-Winkler Token String Score</span>
        <span class="v3d-feat-pct">${(entity.features.jaro * 100).toFixed(1)}%</span>
      </div>
      <div class="v3d-bar-bg"><div class="v3d-bar-fill" style="width:${entity.features.jaro * 100}%; background:${entity.color};"></div></div>

      <div class="v3d-feat-row">
        <span>Token Jaccard / Overlap</span>
        <span class="v3d-feat-pct">${(entity.features.token * 100).toFixed(1)}%</span>
      </div>
      <div class="v3d-bar-bg"><div class="v3d-bar-fill" style="width:${entity.features.token * 100}%; background:${entity.color};"></div></div>

      <div class="v3d-feat-row">
        <span>Geospatial Haversine Proximity</span>
        <span class="v3d-feat-pct">${(entity.features.geo * 100).toFixed(1)}%</span>
      </div>
      <div class="v3d-bar-bg"><div class="v3d-bar-fill" style="width:${entity.features.geo * 100}%; background:${entity.color};"></div></div>

      <div class="v3d-feat-row">
        <span>Normalized Phone E.164 Match</span>
        <span class="v3d-feat-pct">${(entity.features.phone * 100).toFixed(1)}%</span>
      </div>
      <div class="v3d-bar-bg"><div class="v3d-bar-fill" style="width:${entity.features.phone * 100}%; background:${entity.color};"></div></div>

      <div class="v3d-inspect-coords">
        <span>Vector (X, Y, Z):</span>
        <span style="font-family:monospace; color:#A5B4FC;">
          [${entity.umap.x.toFixed(1)}, ${entity.umap.y.toFixed(1)}, ${entity.umap.z.toFixed(1)}]
        </span>
      </div>
    `;

    // Highlight item in sidebar list
    document.querySelectorAll('.v3d-entity-item').forEach(item => {
      item.classList.toggle('active', item.getAttribute('data-id') === entity.id);
    });
  }

  function populateEntityList() {
    const listElem = document.getElementById('v3dEntityList');
    if (!listElem) return;

    listElem.innerHTML = '';
    VECTOR_ENTITIES.forEach(entity => {
      const item = document.createElement('div');
      item.className = 'v3d-entity-item' + (entity.id === 'S1-00001' ? ' active' : '');
      item.setAttribute('data-id', entity.id);
      item.innerHTML = `
        <div class="v3d-item-dot" style="background:${entity.color};"></div>
        <div class="v3d-item-info">
          <div class="v3d-item-name">${entity.name}</div>
          <div class="v3d-item-meta">${entity.id} &middot; ${(entity.similarity * 100).toFixed(1)}%</div>
        </div>
      `;

      item.addEventListener('click', () => {
        selectNode(entity);
        // Smoothly rotate camera toward this node
        const coords = state.currentCoords[entity.id];
        if (coords) {
          state.targetPanX = -coords.x * 0.8;
          state.targetPanY = coords.y * 0.8;
        }
      });

      listElem.appendChild(item);
    });
  }

  function filterEntityList(query) {
    document.querySelectorAll('.v3d-entity-item').forEach(item => {
      const id = item.getAttribute('data-id');
      const entity = VECTOR_ENTITIES.find(e => e.id === id);
      if (!entity) return;

      const matches = !query ||
        entity.name.toLowerCase().includes(query) ||
        entity.id.toLowerCase().includes(query) ||
        entity.classification.toLowerCase().includes(query);

      item.style.display = matches ? 'flex' : 'none';
    });
  }

})();
