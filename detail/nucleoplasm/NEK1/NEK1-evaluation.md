---
type: protein-evaluation
gene: "NEK1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## NEK1 — REJECTED (研究热度过高 (PubMed strict=147，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | NEK1 / KIAA1901 |
| 蛋白名称 | Serine/threonine-protein kinase Nek1 |
| 蛋白大小 | 1258 aa / 142.8 kDa |
| UniProt ID | Q96PY6 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Primary cilium, Centriolar satellite, Cytos; UniProt: Nucleus; Cytoplasm, cytoskeleton, microtubule organizing cen |
| 蛋白大小 | 5/10 | ×1 | 5 | 1258 aa / 142.8 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=147 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=56.9; PDB: 4APC, 4B9D |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR011009, IPR051131, IPR000719, IPR017441, IPR008 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **75.5/180** | |
| **归一化总分** | | | **41.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Primary cilium, Centriolar satellite, Cytosol | Supported |
| UniProt | Nucleus; Cytoplasm, cytoskeleton, microtubule organizing center, centrosome; Cytoplasm | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- centriolar satellite (GO:0034451)
- centrosome (GO:0005813)
- cilium (GO:0005929)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- pericentriolar material (GO:0000242)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 147 |
| PubMed broad count | 256 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA1901 |

**关键文献**:
1. Molecular Mechanisms of TDP-43 Misfolding and Pathology in Amyotrophic Lateral Sclerosis.. *Frontiers in molecular neuroscience*. PMID: 30837838
2. Alterations of DNA damage response pathway: Biomarker and therapeutic strategy for cancer immunotherapy.. *Acta pharmaceutica Sinica. B*. PMID: 34729299
3. Role of genetics in amyotrophic lateral sclerosis: a large cohort study in Chinese mainland population.. *Journal of medical genetics*. PMID: 34544842
4. Dynamic Regulation of ME1 Phosphorylation and Acetylation Affects Lipid Metabolism and Colorectal Tumorigenesis.. *Molecular cell*. PMID: 31735643
5. Mutations in NEK1 cause ciliary dysfunction as a novel pathogenic mechanism in amyotrophic lateral sclerosis.. *Molecular neurodegeneration*. PMID: 40389989

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 56.9 |
| 高置信度残基 (pLDDT>90) 占比 | 16.9% |
| 置信残基 (pLDDT 70-90) 占比 | 26.8% |
| 中等置信 (pLDDT 50-70) 占比 | 6.9% |
| 低置信 (pLDDT<50) 占比 | 49.4% |
| 有序区域 (pLDDT>70) 占比 | 43.7% |
| 可用 PDB 条目 | 4APC, 4B9D |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=56.9），有序残基占 43.7%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011009, IPR051131, IPR000719, IPR017441, IPR008271; Pfam: PF00069 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CFAP410 | 0.982 | 0.609 | — |
| DYNC2H1 | 0.972 | 0.000 | — |
| ALS2 | 0.942 | 0.778 | — |
| KIF3A | 0.802 | 0.230 | — |
| CHCHD10 | 0.733 | 0.000 | — |
| VAPB | 0.717 | 0.000 | — |
| MATR3 | 0.661 | 0.000 | — |
| MATR3-2 | 0.661 | 0.000 | — |
| RCC1L | 0.658 | 0.000 | — |
| CEP290 | 0.635 | 0.112 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000408020.2 | psi-mi:"MI:0018"(two hybrid) | pubmed:14690447 |
| ZNF350 | psi-mi:"MI:0018"(two hybrid) | pubmed:14690447 |
| FEZ2 | psi-mi:"MI:0018"(two hybrid) | pubmed:14690447 |
| FEZ1 | psi-mi:"MI:0018"(two hybrid) | pubmed:14690447 |
| YWHAH | psi-mi:"MI:0018"(two hybrid) | pubmed:14690447 |
| ATRX | psi-mi:"MI:0018"(two hybrid) | pubmed:14690447 |
| MRE11 | psi-mi:"MI:0018"(two hybrid) | pubmed:14690447 |
| TP53BP1 | psi-mi:"MI:0018"(two hybrid) | pubmed:14690447 |
| KIF3A | psi-mi:"MI:0018"(two hybrid) | pubmed:14690447 |
| PPP2R5D | psi-mi:"MI:0018"(two hybrid) | pubmed:14690447 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=56.9 + PDB: 4APC, 4B9D | pLDDT=56.9, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm, cytoskeleton, microtubule orga / Nucleoplasm; 额外: Primary cilium, Centriolar satell | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. NEK1 — Serine/threonine-protein kinase Nek1，研究基础较多，新颖性有限。
2. 蛋白大小1258 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 147 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=56.9），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 147 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96PY6
- Protein Atlas: https://www.proteinatlas.org/ENSG00000137601-NEK1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=NEK1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96PY6
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
