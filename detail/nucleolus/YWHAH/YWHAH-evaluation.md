---
type: protein-evaluation
gene: "YWHAH"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation, rescued]
status: scored
---

## YWHAH 核蛋白评估报告（HPA复核救回）

**救回原因**: 原始评分误判核定位≤3淘汰。HPA IF 实际显示 Nucleoli rim; Nucleoplasm (Reliability: Approved)，确认为核蛋白。

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/YWHAH/IF_images/1319_A11_1_blue_red_green.jpg]]
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/YWHAH/IF_images/1319_A11_3_blue_red_green.jpg]]

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | YWHAH |
| 蛋白名称 | 14-3-3 protein eta |
| 蛋白大小 | 246 aa |
| UniProt ID | [Q04917](https://www.uniprot.org/uniprotkb/Q04917) |
| HPA 核定位 (IF) | Nucleoli rim; Nucleoplasm |
| HPA 可靠性 | Approved |
| PubMed 总数 | 56 |
| AlphaFold pLDDT | 95.2 |

### 2. 评分总览 (权重: 核×4 大×1 新×5 结×3 域×2 PPI×3 ÷1.83)

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 7/10 | ×4 | 28 | HPA IF: Nucleoli rim; Nucleoplasm (Approved); UniProt: N/A |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 246 aa |
| 🆕 研究新颖性 | 6/10 | ×5 | 30 | PubMed 56篇 |
| 🏗️ 三维结构 | 8/10 | ×3 | 24 | AlphaFold pLDDT: 95.2 |
| 🧬 调控结构域 | 6/10 | ×2 | 12 | UniProt domains: None identified |
| 🔗 PPI | 4/10 | ×3 | 12 | 待细化（默认基线） |
| ➕ 互证加分 | — | — | **+0** | 待补充 |
| **原始总分** |  |  | **116/183** |  |
| **归一化总分** |  |  | **63.4/100** |  |

> AlphaFold PAE: 暂无数据或未提供可用 PAE 图；结构判断基于 AlphaFold/PDB 可用记录。
### 3. HPA 核定位证据

HPA 免疫荧光（IF）实验数据确认 YWHAH 定位：
- **亚细胞定位**: Nucleoli rim; Nucleoplasm
- **抗体可靠性**: Approved
- **原始分类**: 核定位 ≤3（误判）→ 经HPA IF复核确认为核蛋白

### 4. UniProt 补充信息

- **亚细胞定位**: N/A
- **结构域**: None identified
- **关键词**: ; ; ; ; ;

### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 查询结果 | 见关键文献 |


**关键文献**:
1. He T et al. (2023). "Extracellular vesicle-circEHD2 promotes the progression of renal cell carcinoma by activating cancer-associated fibroblasts". *Mol Cancer*. PMID: 37481520
2. Huang J et al. (2025). "Snhg18 regulates Yap subcellular localization to maintain bone homeostasis". *Nat Commun*. PMID: 40813368
3. Vlassakev I et al. (2025). "The liver clock modulates circadian rhythms in white adipose tissue". *Mol Metab*. PMID: 40947011
4. Li Q et al. (2025). "YWHAH‑driven autophagy via MAPK/ERK signaling enhances CRC cell migration and invasion". *Int J Mol Med*. PMID: 41133478
5. Yao H et al. (2024). "IMPLICATIONS OF YWHAH GENE EXPRESSION IN THE EARLY DETECTION OF SEPSIS". *Shock*. PMID: 38904460

**评价**: 基于 PubMed 检索结果。


#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| — | — | — | — | — |

**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| — | — | — | — |

**已知复合体成员** (GO Cellular Component):
- 暂无 GO-CC 数据

**IntAct 查询记录**: IntAct: 未检索到实验验证互作

**评价**: 待补充 IntAct/STRING/GO-CC 数据。


### 5. 总体评价

**推荐等级**: ⭐⭐

**核心发现**:
1. **HPA IF 确认为核蛋白**: 原始"核定位≤3"淘汰为误判，HPA实验数据确认为Nucleoli rim; Nucleoplasm
2. **研究新颖性**: PubMed仅56篇文献，属于低研究热度靶点
3. **结构质量**: AlphaFold pLDDT = 95.2

### 6. 数据来源
- [HPA](https://www.proteinatlas.org/search/YWHAH)
- [UniProt](https://www.uniprot.org/uniprotkb/Q04917)
- [PubMed](https://pubmed.ncbi.nlm.nih.gov/?term=YWHAH%5BTitle/Abstract%5D)
- [AlphaFold](https://alphafold.ebi.ac.uk/entry/Q04917)


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。




