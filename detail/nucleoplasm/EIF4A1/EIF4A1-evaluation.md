---
type: protein-evaluation
gene: "EIF4A1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## EIF4A1 — REJECTED (研究热度过高 (PubMed strict=153，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | EIF4A1 / DDX2A, EIF4A |
| 蛋白名称 | Eukaryotic initiation factor 4A-I |
| 蛋白大小 | 406 aa / 46.2 kDa |
| UniProt ID | P60842 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Cytosol; UniProt: Cytoplasm, perinuclear region; Cell membrane; Cytoplasm, Str |
| 蛋白大小 | 10/10 | ×1 | 10 | 406 aa / 46.2 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=153 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=87.1; PDB: 2G9N, 2ZU6, 3EIQ, 5ZBZ, 5ZC9, 6ZMW, 7PPZ |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR011545, IPR044728, IPR014001, IPR001650, IPR027 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **96.0/180** | |
| **归一化总分** | | | **53.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol | Approved |
| UniProt | Cytoplasm, perinuclear region; Cell membrane; Cytoplasm, Stress granule | Swiss-Prot/TrEMBL |

**IF 图像获取**: 尝试获取IF原图中...

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytoplasmic stress granule (GO:0010494)
- cytosol (GO:0005829)
- eukaryotic translation initiation factor 4F complex (GO:0016281)
- extracellular exosome (GO:0070062)
- membrane (GO:0016020)
- nuclear stress granule (GO:0097165)
- perinuclear region of cytoplasm (GO:0048471)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 153 |
| PubMed broad count | 225 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: DDX2A, EIF4A |

**关键文献**:
1. Targeting PGE2 mediated senescent neuron improves tumor therapy.. *Neuro-oncology*. PMID: 39963753
2. Genomic landscape of virus-associated cancers.. *Nature communications*. PMID: 40595559
3. IGF2BP2 Drives Cell Cycle Progression in Triple-Negative Breast Cancer by Recruiting EIF4A1 to Promote the m6A-Modified CDK6 Translation Initiation Process.. *Advanced science (Weinheim, Baden-Wurttemberg, Germany)*. PMID: 37983610
4. Protein translation rate determines neocortical neuron fate.. *Nature communications*. PMID: 38849354
5. CEP112 coordinates translational regulation of essential fertility genes during spermiogenesis through phase separation in humans and mice.. *Nature communications*. PMID: 39349455

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 87.1 |
| 高置信度残基 (pLDDT>90) 占比 | 62.3% |
| 置信残基 (pLDDT 70-90) 占比 | 25.1% |
| 中等置信 (pLDDT 50-70) 占比 | 7.9% |
| 低置信 (pLDDT<50) 占比 | 4.7% |
| 有序区域 (pLDDT>70) 占比 | 87.4% |
| 可用 PDB 条目 | 2G9N, 2ZU6, 3EIQ, 5ZBZ, 5ZC9, 6ZMW, 7PPZ, 7PQ0, 8HUJ, 8OZ0 |


**PAE**: PAE 图像未生成本地文件，结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（2G9N, 2ZU6, 3EIQ, 5ZBZ, 5ZC9, 6ZMW, 7PPZ, 7PQ0, 8HUJ, 8OZ0）+ AlphaFold极高置信度预测（pLDDT=87.1），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011545, IPR044728, IPR014001, IPR001650, IPR027417; Pfam: PF00270, PF00271 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| EIF4E | 0.999 | 0.876 | — |
| PABPC1 | 0.999 | 0.724 | — |
| PDCD4 | 0.999 | 0.985 | — |
| EIF4H | 0.999 | 0.639 | — |
| EIF4G3 | 0.999 | 0.895 | — |
| EIF4G1 | 0.999 | 0.989 | — |
| EIF4B | 0.999 | 0.672 | — |
| EIF4G2 | 0.999 | 0.923 | — |
| EIF3B | 0.998 | 0.970 | — |
| EIF1 | 0.998 | 0.800 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000293831.8 | psi-mi:"MI:2289"(virotrap) | pubmed:37316325|imex:IM-30146 |
| EBI-64041189 | psi-mi:"MI:2289"(virotrap) | pubmed:37316325|imex:IM-30146 |
| MED19 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:15175163 |
| MED10 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:15175163 |
| MED9 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:15175163 |
| MED26 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:15175163 |
| CDKA-1 | psi-mi:"MI:0019"(coimmunoprecipitation) | pubmed:14706832 |
| GRB2 | psi-mi:"MI:0096"(pull down) | pubmed:12577067|mint:MINT-5216 |
| LPPR4 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| EIF4G2 | psi-mi:"MI:0096"(pull down) | pubmed:16166382|imex:IM-18971 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=87.1 + PDB: 2G9N, 2ZU6, 3EIQ, 5ZBZ, 5ZC9,  | pLDDT=87.1, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm, perinuclear region; Cell membrane; Cyto / Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. EIF4A1 — Eukaryotic initiation factor 4A-I，研究基础较多，新颖性有限。
2. 蛋白大小406 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 153 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 153 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P60842
- Protein Atlas: https://www.proteinatlas.org/ENSG00000161960-EIF4A1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=EIF4A1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P60842
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
