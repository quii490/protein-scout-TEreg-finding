---
type: protein-evaluation
gene: "AP3B2"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation, rescued]
status: scored
---

> AlphaFold PAE: 暂无数据或未提供可用 PAE 图；结构判断基于 AlphaFold/PDB 可用记录。
## AP3B2 核蛋白评估报告（HPA复核救回）

**救回原因**: 原始评分误判核定位≤3淘汰。HPA IF 实际显示 Nucleoplasm (Reliability: Approved)，确认为核蛋白。

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/AP3B2/IF_images/560_D12_1_blue_red_green.jpg]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/AP3B2/IF_images/560_D12_2_blue_red_green.jpg]]

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | AP3B2 |
| 蛋白名称 | AP-3 complex subunit beta-2 |
| 蛋白大小 | 1082 aa |
| UniProt ID | [Q13367](https://www.uniprot.org/uniprotkb/Q13367) |
| HPA 核定位 (IF) | Nucleoplasm |
| HPA 可靠性 | Approved |
| PubMed 总数 | 37 |
| AlphaFold pLDDT | 74.9 |

### 2. 评分总览 (权重: 核×4 大×1 新×5 结×3 域×2 PPI×3 ÷1.83)

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 6/10 | ×4 | 24 | HPA IF: Nucleoplasm (Approved); UniProt: Cytoplasmic vesicle, clathrin-coated vesicle membrane; Golgi apparatus |
| 📏 蛋白大小 | 8/10 | ×1 | 8 | 1082 aa |
| 🆕 研究新颖性 | 8/10 | ×5 | 40 | PubMed 37篇 |
| 🏗️ 三维结构 | 6/10 | ×3 | 18 | AlphaFold pLDDT: 74.9 |
| 🧬 调控结构域 | 6/10 | ×2 | 12 | UniProt domains: None identified |
| 🔗 PPI | 4/10 | ×3 | 12 | 待细化（默认基线） |
| ➕ 互证加分 | — | — | **+0** | 待补充 |
| **原始总分** |  |  | **114/183** |  |
| **归一化总分** |  |  | **62.3/100** |  |

### 3. HPA 核定位证据

HPA 免疫荧光（IF）实验数据确认 AP3B2 定位：
- **亚细胞定位**: Nucleoplasm
- **抗体可靠性**: Approved
- **原始分类**: 核定位 ≤3（误判）→ 经HPA IF复核确认为核蛋白

### 4. UniProt 补充信息

- **亚细胞定位**: Cytoplasmic vesicle, clathrin-coated vesicle membrane; Golgi apparatus
- **结构域**: None identified
- **关键词**: ; ; ; ; ; ; ; ; ;

### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 查询结果 | 见关键文献 |


**关键文献**:
1. Narayan RN et al. (2020). "Autoimmune Vestibulocerebellar Syndromes". *Semin Neurol*. PMID: 31958862
2. Honorat JA et al. (2019). "Autoimmune gait disturbance accompanying adaptor protein-3B2-IgG". *Neurology*. PMID: 31371564
3. Mange L et al. (2021). "Cerebellar ataxia and myeloradiculopathy associated with AP3B2 antibody: a case report and literature review". *J Neurol*. PMID: 33988764
4. Walton S et al. (2024). "Neither alpha-synuclein fibril strain nor host murine genotype influences seeding efficacy". *NPJ Parkinsons Dis*. PMID: 38773124
5. Reichlmeir M et al. (2024). "The ataxia-telangiectasia disease protein ATM controls vesicular protein secretion via CHGA and microtubule dynamics via CRMP5". *Neurobiol Dis*. PMID: 39615799

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
2. **研究新颖性**: PubMed仅37篇文献，属于低研究热度靶点
3. **结构质量**: AlphaFold pLDDT = 74.9

### 6. 数据来源
- [HPA](https://www.proteinatlas.org/search/AP3B2)
- [UniProt](https://www.uniprot.org/uniprotkb/Q13367)
- [PubMed](https://pubmed.ncbi.nlm.nih.gov/?term=AP3B2%5BTitle/Abstract%5D)
- [AlphaFold](https://alphafold.ebi.ac.uk/entry/Q13367)


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q13367 |
| SMART | SM01355; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR026740;IPR056314;IPR029390;IPR026739;IPR011989;IPR016024;IPR002553;IPR013041; |
| Pfam | PF01602;PF14796;PF24080; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000103723-AP3B2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| AP3M1 | Biogrid | false |
| AP3S1 | Biogrid | false |
| ARRB2 | Biogrid | false |
| RUFY1 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
