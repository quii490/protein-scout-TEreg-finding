---
type: protein-evaluation
gene: "IAH1"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation, rescued]
status: scored
---

> AlphaFold PAE: 暂无数据或未提供可用 PAE 图；结构判断基于 AlphaFold/PDB 可用记录。
## IAH1 核蛋白评估报告（HPA复核救回）

**救回原因**: 原始评分误判核定位≤3淘汰。HPA IF 实际显示 Nucleoplasm (Reliability: Approved)，确认为核蛋白。

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/IAH1/IF_images/1040_C6_1_blue_red_green.jpg]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/IAH1/IF_images/1040_C6_2_blue_red_green.jpg]]

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | IAH1 |
| 蛋白名称 | Isoamyl acetate-hydrolyzing esterase 1 homolog |
| 蛋白大小 | 248 aa |
| UniProt ID | [Q2TAA2](https://www.uniprot.org/uniprotkb/Q2TAA2) |
| HPA 核定位 (IF) | Nucleoplasm |
| HPA 可靠性 | Approved |
| PubMed 总数 | 0 |
| AlphaFold pLDDT | 93.1 |

### 2. 评分总览 (权重: 核×4 大×1 新×5 结×3 域×2 PPI×3 ÷1.83)

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 6/10 | ×4 | 24 | HPA IF: Nucleoplasm (Approved); UniProt: N/A |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 248 aa |
| 🆕 研究新颖性 | 10/10 | ×5 | 50 | PubMed 0篇 |
| 🏗️ 三维结构 | 8/10 | ×3 | 24 | AlphaFold pLDDT: 93.1 |
| 🧬 调控结构域 | 6/10 | ×2 | 12 | UniProt domains: None identified |
| 🔗 PPI | 4/10 | ×3 | 12 | 待细化（默认基线） |
| ➕ 互证加分 | — | — | **+0** | 待补充 |
| **原始总分** |  |  | **132/183** |  |
| **归一化总分** |  |  | **72.1/100** |  |

### 3. HPA 核定位证据

HPA 免疫荧光（IF）实验数据确认 IAH1 定位：
- **亚细胞定位**: Nucleoplasm
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
1. Kobayashi M et al. (2016). "Detection of differentially expressed candidate genes for a fatty liver QTL on mouse chromosome 12". *BMC Genet*. PMID: 27266874
2. Sun C et al. (2025). "Comprehensive analysis on the implications of IAH1 in cancer development and progression". *Biochem Biophys Rep*. PMID: 41311370
3. Masuya T et al. (2020). "Ablation of Iah1, a candidate gene for diet-induced fatty liver, does not affect liver lipid accumulation in mice". *PLoS One*. PMID: 32407372
4. Li W et al. (2017). "Regulation of Saccharomyces cerevisiae genetic engineering on the production of acetate esters and higher alcohols during Chinese Baijiu fermentation". *J Ind Microbiol Biotechnol*. PMID: 28176138
5. Lilly M et al. (2006). "The effect of increased yeast alcohol acetyltransferase and esterase activity on the flavour profiles of wine and distillates". *Yeast*. PMID: 16845703

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

**推荐等级**: ⭐⭐⭐

**核心发现**:
1. **HPA IF 确认为核蛋白**: 原始"核定位≤3"淘汰为误判，HPA实验数据确认为Nucleoplasm
2. **研究新颖性**: PubMed仅0篇文献，属于低研究热度靶点
3. **结构质量**: AlphaFold pLDDT = 93.1

### 6. 数据来源
- [HPA](https://www.proteinatlas.org/search/IAH1)
- [UniProt](https://www.uniprot.org/uniprotkb/Q2TAA2)
- [PubMed](https://pubmed.ncbi.nlm.nih.gov/?term=IAH1%5BTitle/Abstract%5D)
- [AlphaFold](https://alphafold.ebi.ac.uk/entry/Q2TAA2)


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q2TAA2 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR001087;IPR045136;IPR036514; |
| Pfam | PF00657; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000134330-IAH1/interaction

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
