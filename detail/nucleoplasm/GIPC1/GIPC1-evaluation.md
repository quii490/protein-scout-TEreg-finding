---
type: protein-evaluation
gene: "GIPC1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## GIPC1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GIPC1 / C19orf3, GIPC, RGS19IP1 |
| 蛋白名称 | PDZ domain-containing protein GIPC1 |
| 蛋白大小 | 333 aa / 36.0 kDa |
| UniProt ID | O14908 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Plasma membrane, Cell Junctions; 额外: Nucleoplasm; UniProt: Cytoplasm; Membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 333 aa / 36.0 kDa |
| 研究新颖性 | 2/10 | ×5 | 10 | PubMed strict=100 篇 (≤100→2) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=80.5; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR055349, IPR056814, IPR017379, IPR001478, IPR036 |
| PPI 网络 | 2/10 | ×3 | 6 | STRING 0 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **80.0/180** | |
| **归一化总分** | | | **44.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Plasma membrane, Cell Junctions; 额外: Nucleoplasm | Approved |
| UniProt | Cytoplasm; Membrane | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cell cortex (GO:0005938)
- cytoplasm (GO:0005737)
- cytoplasmic vesicle (GO:0031410)
- cytosol (GO:0005829)
- dendritic shaft (GO:0043198)
- dendritic spine (GO:0043197)
- extracellular exosome (GO:0070062)
- glutamatergic synapse (GO:0098978)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 100 |
| PubMed broad count | 212 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C19orf3, GIPC, RGS19IP1 |

**关键文献**:
1. Oculopharyngodistal myopathy.. *Current opinion in neurology*. PMID: 35942670
2. BDNF-induced local protein synthesis and synaptic plasticity.. *Neuropharmacology*. PMID: 23602987
3. Neuropilin-1 inhibition suppresses nerve growth factor signaling and nociception in pain models.. *The Journal of clinical investigation*. PMID: 39589827
4. GIPC1 regulates MACC1-driven metastasis.. *Frontiers in oncology*. PMID: 38144523
5. Heat-shock chaperone HSPB1 mitigates poly-glycine-induced neurodegeneration via restoration of autophagic flux.. *Autophagy*. PMID: 39936620

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 80.5 |
| 高置信度残基 (pLDDT>90) 占比 | 58.0% |
| 置信残基 (pLDDT 70-90) 占比 | 16.8% |
| 中等置信 (pLDDT 50-70) 占比 | 4.8% |
| 低置信 (pLDDT<50) 占比 | 20.4% |
| 有序区域 (pLDDT>70) 占比 | 74.8% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 中等质量（pLDDT=80.5，有序区 74.8%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR055349, IPR056814, IPR017379, IPR001478, IPR036034; Pfam: PF25083, PF25082, PF00595 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| — | — | — | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Lrp2 | psi-mi:"MI:0018"(two hybrid) | pubmed:10827173 |
| ZNF408 | psi-mi:"MI:0018"(two hybrid) | pubmed:15231747 |
| ADRB1 | psi-mi:"MI:0081"(peptide array) | imex:IM-14531|pubmed:16316992 |
| SSR4 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| PDXDC1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| COPB2 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| MCM7 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| NOC2L | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| MMS19 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| ENSP00000466747.1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |

**PPI 互证分析**:
- 仅IntAct实验
- STRING partners: 0，IntAct interactions: 15
- 调控相关比例: 0 / 0 = 0%

**评价**: STRING 0 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=80.5 + PDB: 无 | pLDDT=80.5, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Membrane / Plasma membrane, Cell Junctions; 额外: Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 0 + 15 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐

**核心优势**:
1. GIPC1 — PDZ domain-containing protein GIPC1，研究基础较多，新颖性有限。
2. 蛋白大小333 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 100 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O14908
- Protein Atlas: https://www.proteinatlas.org/ENSG00000123159-GIPC1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GIPC1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O14908
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
