---
type: protein-evaluation
gene: "DIP2C"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation, rescued]
status: scored
---

> AlphaFold PAE: 暂无数据或未提供可用 PAE 图；结构判断基于 AlphaFold/PDB 可用记录。
## DIP2C 核蛋白评估报告（HPA复核救回）

**IF 图像

![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/DIP2C/IF_images/DIP2C_BJ_2.jpg]]**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/DIP2C/IF_images/DIP2C_BJ_1.jpg]]

**救回原因**: 原始评分误判核定位≤3淘汰。HPA IF 实际显示 Nucleoplasm (Reliability: Approved)，确认为核蛋白。

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | DIP2C |
| 蛋白名称 | Disco-interacting protein 2 homolog C |
| 蛋白大小 | 1556 aa |
| UniProt ID | [Q9Y2E4](https://www.uniprot.org/uniprotkb/Q9Y2E4) |
| HPA 核定位 (IF) | Nucleoplasm |
| HPA 可靠性 | Approved |
| PubMed 总数 | 42 |
| AlphaFold pLDDT | 79.5 |

### 2. 评分总览 (权重: 核×4 大×1 新×5 结×3 域×2 PPI×3 ÷1.83)

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 6/10 | ×4 | 24 | HPA IF: Nucleoplasm (Approved); UniProt: N/A |
| 📏 蛋白大小 | 5/10 | ×1 | 5 | 1556 aa |
| 🆕 研究新颖性 | 6/10 | ×5 | 30 | PubMed 42篇 |
| 🏗️ 三维结构 | 7/10 | ×3 | 21 | AlphaFold pLDDT: 79.5 |
| 🧬 调控结构域 | 6/10 | ×2 | 12 | UniProt domains: None identified |
| 🔗 PPI | 4/10 | ×3 | 12 | 待细化（默认基线） |
| ➕ 互证加分 | — | — | **+0** | 待补充 |
| **原始总分** |  |  | **104/183** |  |
| **归一化总分** |  |  | **56.8/100** |  |

### 3. HPA 核定位证据

HPA 免疫荧光（IF）实验数据确认 DIP2C 定位：
- **亚细胞定位**: Nucleoplasm
- **抗体可靠性**: Approved
- **原始分类**: 核定位 ≤3（误判）→ 经HPA IF复核确认为核蛋白

### 4. UniProt 补充信息

- **亚细胞定位**: N/A
- **结构域**: None identified
- **关键词**: ; ; ;

### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 查询结果 | 见关键文献 |


**关键文献**:
1. Ha T et al. (2024). "De novo variants predicting haploinsufficiency for DIP2C are associated with expressive speech delay". *Am J Med Genet A*. PMID: 38421105
2. Maddirevula S et al. (2018). "Expanding the phenome and variome of skeletal dysplasia". *Genet Med*. PMID: 29620724
3. Yang L et al. (2022). "Novel DIP2C gene splicing variant in an individual with focal infantile epilepsy". *Am J Med Genet A*. PMID: 34617658
4. Yao M et al. (2021). "Knockout of Dip2c in murine ES cell line IBMSe001-B-1 by CRISPR/Cas9 genome editing technology". *Stem Cell Res*. PMID: 33813174
5. Li Y et al. (2022). "DIP2C polymorphisms are implicated in susceptibility and clinical phenotypes of autism spectrum disorder". *Psychiatry Res*. PMID: 35987071

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
2. **研究新颖性**: PubMed仅42篇文献，属于低研究热度靶点
3. **结构质量**: AlphaFold pLDDT = 79.5

### 6. 数据来源
- [HPA](https://www.proteinatlas.org/search/DIP2C)
- [UniProt](https://www.uniprot.org/uniprotkb/Q9Y2E4)
- [PubMed](https://pubmed.ncbi.nlm.nih.gov/?term=DIP2C%5BTitle/Abstract%5D)
- [AlphaFold](https://alphafold.ebi.ac.uk/entry/Q9Y2E4)


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
| UniProt | Q9Y2E4 |
| SMART | SM01137; |
| UniProt Domain [FT] | DOMAIN 7..120; /note="DMAP1-binding"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU01260" |
| InterPro | IPR025110;IPR045851;IPR000873;IPR042099;IPR037337;IPR010506; |
| Pfam | PF00501;PF23024;PF06464; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000151240-DIP2C/interaction

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
