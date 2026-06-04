---
type: protein-evaluation
gene: "EIF4E2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## EIF4E2 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | EIF4E2 / EIF4EL3 |
| 蛋白名称 | Eukaryotic translation initiation factor 4E type 2 |
| 蛋白大小 | 245 aa / 28.4 kDa |
| UniProt ID | O60573 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: Mitochondria; 额外: Cytosol; UniProt: Cytoplasm; Cytoplasm, P-body |
| 蛋白大小 | 10/10 | ×1 | 10 | 245 aa / 28.4 kDa |
| 研究新颖性 | 2/10 | ×5 | 10 | PubMed strict=86 篇 (≤100→2) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=80.3; PDB: 2JGB, 2JGC, 5NVK, 5NVL, 5NVM, 5NVN, 5XLN |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR023398, IPR001040, IPR019770; Pfam: PF01652 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **86.0/180** | |
| **归一化总分** | | | **47.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Mitochondria; 额外: Cytosol | Approved |
| UniProt | Cytoplasm; Cytoplasm, P-body | Swiss-Prot/TrEMBL |

**IF 图像获取**: 尝试获取IF原图中...

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- eukaryotic translation initiation factor 4F complex (GO:0016281)
- P-body (GO:0000932)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 86 |
| PubMed broad count | 124 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: EIF4EL3 |

**关键文献**:
1. EDF1 coordinates cellular responses to ribosome collisions.. *eLife*. PMID: 32744497
2. NITAC-mediated ISGylation of eIF4E2 attenuates GSK3β proline-directed kinase activity, conferring cytoprotection.. *The Journal of biological chemistry*. PMID: 41022323
3. Dysregulated RBM24 phosphorylation impairs APOE translation underlying psychological stress-induced cardiovascular disease.. *Nature communications*. PMID: 39580475
4. PARP inhibitor radiosensitization enhances anti-PD-L1 immunotherapy through stabilizing chemokine mRNA in small cell lung cancer.. *Nature communications*. PMID: 40038278
5. eIF4E-homologous protein (4EHP): a multifarious cap-binding protein.. *The FEBS journal*. PMID: 34758096

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 80.3 |
| 高置信度残基 (pLDDT>90) 占比 | 61.6% |
| 置信残基 (pLDDT 70-90) 占比 | 11.0% |
| 中等置信 (pLDDT 50-70) 占比 | 3.7% |
| 低置信 (pLDDT<50) 占比 | 23.7% |
| 有序区域 (pLDDT>70) 占比 | 72.6% |
| 可用 PDB 条目 | 2JGB, 2JGC, 5NVK, 5NVL, 5NVM, 5NVN, 5XLN |


**PAE**: PAE 图像未生成本地文件，结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（2JGB, 2JGC, 5NVK, 5NVL, 5NVM, 5NVN, 5XLN）+ AlphaFold极高置信度预测（pLDDT=80.3），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR023398, IPR001040, IPR019770; Pfam: PF01652 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| GIGYF2 | 0.999 | 0.986 | — |
| GIGYF1 | 0.997 | 0.983 | — |
| EIF4EBP1 | 0.997 | 0.967 | — |
| EIF4G3 | 0.995 | 0.091 | — |
| RBM4 | 0.995 | 0.292 | — |
| EIF4A1 | 0.979 | 0.000 | — |
| EIF4G1 | 0.978 | 0.091 | — |
| EPAS1 | 0.955 | 0.292 | — |
| EIF4G2 | 0.949 | 0.091 | — |
| NCBP2 | 0.941 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| EIF4ENIF1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| EIF4EBP3 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| EIF4EBP1 | psi-mi:"MI:0019"(coimmunoprecipitation) | pubmed:15094042 |
| KRTAP4-12 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| EIF4G1 | psi-mi:"MI:0096"(pull down) | pubmed:15153109|imex:IM-19604 |
| EIF4EBP2 | psi-mi:"MI:0047"(far western blotting) | pubmed:15153109|imex:IM-19604 |
| TRAF6 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| prfA | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| KRT20 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| - | psi-mi:"MI:0004"(affinity chromatography technolog | pubmed:16739988|imex:IM-19402 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 2 / 15 = 13%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 13%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=80.3 + PDB: 2JGB, 2JGC, 5NVK, 5NVL, 5NVM,  | pLDDT=80.3, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Cytoplasm, P-body / Mitochondria; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. EIF4E2 — Eukaryotic translation initiation factor 4E type 2，研究基础较多，新颖性有限。
2. 蛋白大小245 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 86 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O60573
- Protein Atlas: https://www.proteinatlas.org/ENSG00000135930-EIF4E2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=EIF4E2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O60573
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
