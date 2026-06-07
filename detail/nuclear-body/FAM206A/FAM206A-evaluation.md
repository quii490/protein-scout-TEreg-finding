---
type: protein-evaluation
gene: "FAM206A"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## FAM206A 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FAM206A / C9orf6, FAM206A |
| 蛋白名称 | Protein Abitram |
| 蛋白大小 | 181 aa / 20.4 kDa |
| UniProt ID | Q9NX38 |
| 评估日期 | 2026-06-03 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nuclear-body/FAM206A/IF_images/MCF-7_1.jpg|MCF-7]]
![[Projects/TEreg-finding/protein-interested/detail/nuclear-body/FAM206A/IF_images/U2OS_1.jpg|U2OS]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Cytosol; 额外: Kinetochore, Cytokinetic bridge, M; UniProt: Nucleus speckle; Cell projection, lamellipodium; Nucleus; Ce |
| 蛋白大小 | 8/10 | ×1 | 8 | 181 aa / 20.4 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=0 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=79.7; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR039169, IPR033753, IPR011053; Pfam: PF01597 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 5 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **131.5/180** | |
| **归一化总分** | | | **73.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Cytosol; 额外: Kinetochore, Cytokinetic bridge, Mitotic spindle, Primary cilium, Primary cilium tip | Approved |
| UniProt | Nucleus speckle; Cell projection, lamellipodium; Nucleus; Cell projection, growth cone; Cell project... | Swiss-Prot/TrEMBL |

**IF 图像获取**: IF图像已下载并嵌入 (2张)

**GO Cellular Component**:
- dendrite (GO:0030425)
- filopodium tip (GO:0032433)
- growth cone (GO:0030426)
- lamellipodium (GO:0030027)
- nuclear speck (GO:0016607)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 0 |
| PubMed broad count | 0 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C9orf6, FAM206A |

**关键文献**:
无关键文献数据。

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 79.7 |
| 高置信度残基 (pLDDT>90) 占比 | 9.4% |
| 置信残基 (pLDDT 70-90) 占比 | 68.0% |
| 中等置信 (pLDDT 50-70) 占比 | 21.5% |
| 低置信 (pLDDT<50) 占比 | 1.1% |
| 有序区域 (pLDDT>70) 占比 | 77.4% |
| 可用 PDB 条目 | 无 |


**PAE (Predicted Aligned Error)**:
![[Projects/TEreg-finding/protein-interested/detail/nuclear-body/FAM206A/FAM206A-PAE.png]]

**评价**: AlphaFold 中等质量（pLDDT=79.7，有序区 77.4%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR039169, IPR033753, IPR011053; Pfam: PF01597 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| FRRS1L | 0.882 | 0.000 | — |
| PEX26 | 0.879 | 0.000 | — |
| PEX6 | 0.866 | 0.000 | — |
| SYNJ2BP | 0.826 | 0.000 | — |
| PUS10 | 0.801 | 0.801 | — |
| GPN3 | 0.540 | 0.000 | — |
| ELP1 | 0.524 | 0.000 | — |
| SPRYD7 | 0.459 | 0.000 | — |
| C8A | 0.453 | 0.000 | — |
| CTNNAL1 | 0.453 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| HMBOX1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| MESD | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| ABITRAM | psi-mi:"MI:1356"(validated two hybrid) | imex:IM-23318|pubmed:25416956 |
| PUS10 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| PGCKA1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 5
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 5 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=79.7 + PDB: 无 | pLDDT=79.7, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus speckle; Cell projection, lamellipodium; N / Nucleoplasm, Cytosol; 额外: Kinetochore, Cytokinetic | 一致 |
| PPI | STRING + IntAct | 15 + 5 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. FAM206A — Protein Abitram，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小181 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 0 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NX38
- Protein Atlas: https://www.proteinatlas.org/ENSG00000119328-ABITRAM/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FAM206A
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NX38
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nuclear-body/FAM206A/FAM206A-PAE.png]]

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9NX38 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR039169;IPR033753;IPR011053; |
| Pfam | PF01597; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000119328-ABITRAM/interaction

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
