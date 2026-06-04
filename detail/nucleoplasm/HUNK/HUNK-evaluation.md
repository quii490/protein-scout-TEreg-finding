---
type: protein-evaluation
gene: "HUNK"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation, rescued]
status: scored
---

## HUNK 核蛋白评估报告（HPA复核救回）

**救回原因**: 原始评分误判核定位≤3淘汰。HPA IF 实际显示 Nucleoplasm (Reliability: Approved)，确认为核蛋白。

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/HUNK/IF_images/2231_E8_1_blue_red_green.jpg]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/HUNK/IF_images/2231_E8_2_blue_red_green.jpg]]

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | HUNK |
| 蛋白名称 | Hormonally up-regulated neu tumor-associated kinase |
| 蛋白大小 | 714 aa |
| UniProt ID | [P57058](https://www.uniprot.org/uniprotkb/P57058) |
| HPA 核定位 (IF) | Nucleoplasm |
| HPA 可靠性 | Approved |
| PubMed 总数 | 29 |
| AlphaFold pLDDT | 62.0 |

### 2. 评分总览 (权重: 核×4 大×1 新×5 结×3 域×2 PPI×3 ÷1.83)

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 6/10 | ×4 | 24 | HPA IF: Nucleoplasm (Approved); UniProt: N/A |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 714 aa |
| 🆕 研究新颖性 | 8/10 | ×5 | 40 | PubMed 29篇 |
| 🏗️ 三维结构 | 6/10 | ×3 | 18 | AlphaFold pLDDT: 62.0 |
| 🧬 调控结构域 | 6/10 | ×2 | 12 | UniProt domains: None identified |
| 🔗 PPI | 4/10 | ×3 | 12 | 待细化（默认基线） |
| ➕ 互证加分 | — | — | **+0** | 待补充 |
| **原始总分** |  |  | **116/183** |  |
| **归一化总分** |  |  | **63.4/100** |  |

> AlphaFold PAE: 暂无数据或未提供可用 PAE 图；结构判断基于 AlphaFold/PDB 可用记录。
### 3. HPA 核定位证据

HPA 免疫荧光（IF）实验数据确认 HUNK 定位：
- **亚细胞定位**: Nucleoplasm
- **抗体可靠性**: Approved
- **原始分类**: 核定位 ≤3（误判）→ 经HPA IF复核确认为核蛋白

### 4. UniProt 补充信息

- **亚细胞定位**: N/A
- **结构域**: None identified
- **关键词**: ; ; ; ; ; ;

### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 查询结果 | 见关键文献 |


**关键文献**:
1. Ramos-Solis N et al. (2022). "HUNK Gene Alterations in Breast Cancer". *Biomedicines*. PMID: 36551828
2. Zambrano JN et al. (2018). "Staurosporine, an inhibitor of hormonally up-regulated neu-associated kinase". *Oncotarget*. PMID: 30542510
3. Zambrano JN et al. (2017). "Hormonally up-regulated neu-associated kinase: A novel target for breast cancer progression". *Pharmacol Res*. PMID: 28189783
4. Jiang S et al. (2023). "Hypoxia inhibits HUNK kinase activity to induce epithelial-mesenchymal transition". *Biochem Biophys Res Commun*. PMID: 37793312
5. Dilday T et al. (2020). "HUNK Signaling in Metastatic Breast Cancer". *Oncoscience*. PMID: 32676513

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
1. **HPA IF 确认为核蛋白**: 原始"核定位≤3"淘汰为误判，HPA实验数据确认为Nucleoplasm
2. **研究新颖性**: PubMed仅29篇文献，属于低研究热度靶点
3. **结构质量**: AlphaFold pLDDT = 62.0

### 6. 数据来源
- [HPA](https://www.proteinatlas.org/search/HUNK)
- [UniProt](https://www.uniprot.org/uniprotkb/P57058)
- [PubMed](https://pubmed.ncbi.nlm.nih.gov/?term=HUNK%5BTitle/Abstract%5D)
- [AlphaFold](https://alphafold.ebi.ac.uk/entry/P57058)


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。




