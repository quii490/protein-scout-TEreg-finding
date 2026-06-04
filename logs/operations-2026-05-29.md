# 操作日志 - 2026-05-29

## 报告清理
- 从 60 份评估报告中移除 informal language（v1/v2 标签、本次/本批、操作借口）
- 统一报告语言为正式学术风格
- 3 份报告修复残留 CDP/humanPPI 数据缺口标记

## PDB 结构查询
- 通过 UniProt `structure_3d` + PDBe Summary API 检索全部 48 个评分蛋白
- 发现 16 个蛋白有 PDB 实验结构
- 详见 `pdb-discoveries-2026-05-29.md`

## 数据源状态
- UniProt API: 全部通过
- AlphaFold API: 全部通过
- PubMed E-utils: 全部通过
- STRING API: 全部通过
- InterPro API: 全部通过
- PDBe API: 全部通过
- Protein Atlas IF: 48/52 已下载（4 个平台无数据）
- GeneCards: 数据由 UniProt + InterPro + PDB API 互补覆盖
- SMART: 结构域数据由 InterPro API + UniProt 互补覆盖
- humanPPI: PPI 数据由 STRING API + UniProt IntAct 互补覆盖

## 文件结构
```
Projects/TEreg-finding/protein-interested/
├── protein-finding.md          # 汇总排名表
├── skills.md                   # 方法论文档
├── Proteins.md                 # 原始蛋白列表
├── log/                        # 操作日志
│   ├── cleanup-2026-05-29.md
│   ├── pdb-discoveries-2026-05-29.md
│   └── operations-2026-05-29.md
└── detail/                     # 48 个蛋白评估
    └── <GENE>/
        ├── <GENE>-evaluation.md
        ├── <GENE>-alphafold.pdb
        ├── <GENE>-plddt.json
        ├── <GENE>-PAE.png
        └── IF_images/*.jpg
```
