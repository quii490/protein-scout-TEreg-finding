---
type: protein-evaluation
gene: "INPP5E"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## INPP5E — REJECTED (研究热度过高 (PubMed strict=101，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | INPP5E |
| 蛋白名称 | Phosphatidylinositol polyphosphate 5-phosphatase type IV |
| 蛋白大小 | 644 aa / 70.2 kDa |
| UniProt ID | Q9NRR6 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Golgi apparatus; 额外: Nucleoplasm, Focal adhesion sites; UniProt: Cytoplasm, cytoskeleton, cilium axoneme; Golgi apparatus, Go |
| 蛋白大小 | 10/10 | ×1 | 10 | 644 aa / 70.2 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=101 篇 (>100→REJECTED) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=71.2; PDB: 2XSW |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR036691, IPR042478, IPR000300; Pfam: PF22669 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **87.0/180** | |
| **归一化总分** | | | **48.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Golgi apparatus; 额外: Nucleoplasm, Focal adhesion sites | Uncertain |
| UniProt | Cytoplasm, cytoskeleton, cilium axoneme; Golgi apparatus, Golgi stack membrane; Cell membrane; Cell ... | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- axoneme (GO:0005930)
- cilium (GO:0005929)
- cytosol (GO:0005829)
- Golgi apparatus (GO:0005794)
- Golgi cisterna membrane (GO:0032580)
- Golgi membrane (GO:0000139)
- nucleus (GO:0005634)
- plasma membrane (GO:0005886)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 101 |
| PubMed broad count | 149 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Joubert Syndrome.. **. PMID: 20301500
2. Mechanism and dynamics of INPP5E transport into and inside the ciliary compartment.. *Biological chemistry*. PMID: 29140789
3. Inpp5e is crucial for photoreceptor outer segment maintenance.. *Journal of cell science*. PMID: 39871753
4. Inpp5e Regulated the Cilium-Related Genes Contributing to the Neural Tube Defects Under 5-Fluorouracil Exposure.. *Molecular neurobiology*. PMID: 38285286
5. INPP5E regulates CD3ζ enrichment at the immune synapse by phosphoinositide distribution control.. *Communications biology*. PMID: 37670137

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 71.2 |
| 高置信度残基 (pLDDT>90) 占比 | 49.5% |
| 置信残基 (pLDDT 70-90) 占比 | 5.1% |
| 中等置信 (pLDDT 50-70) 占比 | 5.7% |
| 低置信 (pLDDT<50) 占比 | 39.6% |
| 有序区域 (pLDDT>70) 占比 | 54.6% |
| 可用 PDB 条目 | 2XSW |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 高质量预测（pLDDT=71.2，有序区 54.6%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR036691, IPR042478, IPR000300; Pfam: PF22669 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PDE6D | 0.980 | 0.628 | — |
| ARL13B | 0.956 | 0.000 | — |
| PIP5K1B | 0.944 | 0.000 | — |
| INPP4A | 0.943 | 0.000 | — |
| PIP5K1C | 0.939 | 0.000 | — |
| INPP4B | 0.937 | 0.000 | — |
| OCRL | 0.936 | 0.000 | — |
| INPP5B | 0.932 | 0.000 | — |
| PIP4P2 | 0.930 | 0.000 | — |
| SYNJ2 | 0.929 | 0.067 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| BMPR2 | psi-mi:"MI:0096"(pull down) | pubmed:15188402 |
| - | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| "BEST:LD39762" | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| bdg | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| MARK2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| YWHAH | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| YWHAB | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CA5A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| HSPD1 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| MGST3 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=71.2 + PDB: 2XSW | pLDDT=71.2, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm, cytoskeleton, cilium axoneme; Golgi app / Golgi apparatus; 额外: Nucleoplasm, Focal adhesion s | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. INPP5E — Phosphatidylinositol polyphosphate 5-phosphatase type IV，研究基础较多，新颖性有限。
2. 蛋白大小644 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 101 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 101 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NRR6
- Protein Atlas: https://www.proteinatlas.org/ENSG00000148384-INPP5E/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=INPP5E
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NRR6
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Golgi apparatus (uncertain)。来源: https://www.proteinatlas.org/ENSG00000148384-INPP5E/subcellular

![](https://images.proteinatlas.org/65758/2129_C11_15_blue_red_green.jpg)
![](https://images.proteinatlas.org/65758/2129_C11_38_blue_red_green.jpg)
![](https://images.proteinatlas.org/65758/2161_F4_21_blue_red_green.jpg)
![](https://images.proteinatlas.org/65758/2161_F4_8_blue_red_green.jpg)
![](https://images.proteinatlas.org/65758/2185_B6_22_blue_red_green.jpg)
![](https://images.proteinatlas.org/65758/2185_B6_36_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9NRR6-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9NRR6 |
| SMART | SM00128; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR036691;IPR042478;IPR000300; |
| Pfam | PF22669; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000148384-INPP5E/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| PDE6D | Intact, Biogrid | true |
| YWHAB | Biogrid, Opencell | true |
| YWHAE | Intact, Biogrid, Opencell | true |
| YWHAG | Biogrid, Opencell | true |
| YWHAH | Intact, Biogrid, Opencell | true |
| HNRNPH2 | Opencell | false |
| YWHAZ | Opencell | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
