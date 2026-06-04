---
type: protein-evaluation
gene: "TTC8"
date: 2026-05-30
tags: [protein-scout, nuclear-protein, evaluation, rescued]
status: scored
---

> AlphaFold PAE: 暂无数据或未提供可用 PAE 图；结构判断基于 AlphaFold/PDB 可用记录。
## TTC8 核蛋白评估报告（HPA复核救回）

**救回原因**: 原始评分误判核定位≤3淘汰。HPA IF 实际显示 Nucleoli fibrillar center (Reliability: Approved)，确认为核蛋白。

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/TTC8/IF_images/2167_E1_13_blue_red_green.jpg]]
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/TTC8/IF_images/2167_E1_14_blue_red_green.jpg]]

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | TTC8 |
| 蛋白名称 | Tetratricopeptide repeat protein 8 |
| 蛋白大小 | 541 aa |
| UniProt ID | [Q8TAM2](https://www.uniprot.org/uniprotkb/Q8TAM2) |
| HPA 核定位 (IF) | Nucleoli fibrillar center |
| HPA 可靠性 | Approved |
| PubMed 总数 | 15 |
| AlphaFold pLDDT | 84.2 |

### 2. 评分总览 (权重: 核×4 大×1 新×5 结×3 域×2 PPI×3 ÷1.83)

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 6/10 | ×4 | 24 | HPA IF: Nucleoli fibrillar center (Approved); UniProt: Cytoplasm, cytoskeleton, microtubule organizing center, centrosome; Cell projection, cilium membrane |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 541 aa |
| 🆕 研究新颖性 | 10/10 | ×5 | 50 | PubMed 15篇 |
| 🏗️ 三维结构 | 7/10 | ×3 | 21 | AlphaFold pLDDT: 84.2 |
| 🧬 调控结构域 | 6/10 | ×2 | 12 | UniProt domains: None identified |
| 🔗 PPI | 4/10 | ×3 | 12 | 待细化（默认基线） |
| ➕ 互证加分 | — | — | **+0** | 待补充 |
| **原始总分** |  |  | **129/183** |  |
| **归一化总分** |  |  | **70.5/100** |  |

### 3. HPA 核定位证据

HPA 免疫荧光（IF）实验数据确认 TTC8 定位：
- **亚细胞定位**: Nucleoli fibrillar center
- **抗体可靠性**: Approved
- **原始分类**: 核定位 ≤3（误判）→ 经HPA IF复核确认为核蛋白

### 4. UniProt 补充信息

- **亚细胞定位**: Cytoplasm, cytoskeleton, microtubule organizing center, centrosome; Cell projection, cilium membrane; Cytoplasm; Cytoplasm, cytoskeleton, microtubule organizing center, centrosome, centriolar satellite; Cell projection, cilium
- **结构域**: None identified
- **关键词**: ; ; ; ; ; ; ; ; ;

### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed 查询结果 | 见关键文献 |


**关键文献**:
1. Adam MP et al. (1993). "Nonsyndromic Retinitis Pigmentosa Overview". **. PMID: 20301590
2. Adam MP et al. (1993). "Bardet-Biedl Syndrome Overview". **. PMID: 20301537
3. Chattannavar G et al. (2024). "Bardet-Biedl syndrome with chorioretinal coloboma: a case series and review of literature". *Ophthalmic Genet*. PMID: 39402987
4. Qin Y et al. (2025). "Prenatal diagnosis of fetuses with renal abnormalities: a retrospective analysis of 329 Chinese cases". *Orphanet J Rare Dis*. PMID: 40993696
5. Day WG et al. (2020). "Synchronous Teledermoscopy in Military Treatment Facilities". *Mil Med*. PMID: 32307547

**评价**: 基于 PubMed 检索结果。


#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| Sstr3 | pull down | 20603001 | — | — |
| BBS1 | cosedimentation through density gradient | 17574030 | — | — |
| BBS9 | anti tag coimmunoprecipitation | 17574030 | — | — |
| Bbs2 | molecular sieving | 22072986 | — | — |
| LZTFL1 | inference by socio-affinity scoring | unassigned1312 | — | — |
| BBS5 | inference by socio-affinity scoring | unassigned1312 | — | — |
| BBIP1 | inference by socio-affinity scoring | unassigned1312 | — | — |
| BBS7 | inference by socio-affinity scoring | unassigned1312 | — | — |
| BBS4 | inference by socio-affinity scoring | unassigned1312 | — | — |
| BBS2 | inference by socio-affinity scoring | unassigned1312 | — | — |

**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| — | — | — | — |

**已知复合体成员** (GO Cellular Component):
- 暂无 GO-CC 数据

**IntAct 查询记录**: IntAct: 15 实验验证互作

**评价**: 基于 IntAct + UniProt GO-CC 综合分析。


### 5. 总体评价

**推荐等级**: ⭐⭐⭐

**核心发现**:
1. **HPA IF 确认为核蛋白**: 原始"核定位≤3"淘汰为误判，HPA实验数据确认为Nucleoli fibrillar center
2. **研究新颖性**: PubMed仅15篇文献，属于低研究热度靶点
3. **结构质量**: AlphaFold pLDDT = 84.2

### 6. 数据来源
- [HPA](https://www.proteinatlas.org/search/TTC8)
- [UniProt](https://www.uniprot.org/uniprotkb/Q8TAM2)
- [PubMed](https://pubmed.ncbi.nlm.nih.gov/?term=TTC8%5BTitle/Abstract%5D)
- [AlphaFold](https://alphafold.ebi.ac.uk/entry/Q8TAM2)


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。




