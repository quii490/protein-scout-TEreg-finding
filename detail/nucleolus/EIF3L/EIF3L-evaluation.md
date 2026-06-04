---
type: protein-evaluation
gene: "EIF3L"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## EIF3L 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | EIF3L / EIF3EIP, EIF3S6IP |
| 蛋白名称 | Eukaryotic translation initiation factor 3 subunit L |
| 蛋白大小 | 564 aa / 66.7 kDa |
| UniProt ID | Q9Y262 |
| 评估日期 | 2026-06-03 |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/EIF3L/IF_images/A-431_1.jpg|A-431]]
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/EIF3L/IF_images/U-251MG_1.jpg|U-251MG]]

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoli; 额外: Nucleoplasm; UniProt: Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 564 aa / 66.7 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=22 篇 (≤40→8) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=68.8; PDB: 3J8B, 3J8C, 6FEC, 6YBD, 6ZMW, 6ZON, 6ZP4 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR019382, IPR000717, IPR011990; Pfam: PF10255 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **121.5/180** | |
| **归一化总分** | | | **67.5/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli; 额外: Nucleoplasm | Approved |
| UniProt | Cytoplasm | Swiss-Prot/TrEMBL |

**IF 图像获取**: IF图像已下载并嵌入 (2张)

**GO Cellular Component**:
- cytosol (GO:0005829)
- eukaryotic 43S preinitiation complex (GO:0016282)
- eukaryotic 48S preinitiation complex (GO:0033290)
- eukaryotic translation initiation factor 3 complex (GO:0005852)
- fibrillar center (GO:0001650)
- membrane (GO:0016020)
- nucleoplasm (GO:0005654)
- synapse (GO:0045202)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 22 |
| PubMed broad count | 37 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: EIF3EIP, EIF3S6IP |

**关键文献**:
1. 4EHP and NELF-E regulate physiological ATF4 induction and proteostasis in disease models of Drosophila.. *Nature communications*. PMID: 41436469
2. Mutations in Nonessential eIF3k and eIF3l Genes Confer Lifespan Extension and Enhanced Resistance to ER Stress in Caenorhabditis elegans.. *PLoS genetics*. PMID: 27690135
3. Biophysical and structural characterization of the recombinant human eIF3L.. *Protein and peptide letters*. PMID: 23919378
4. The eukaryotic translation initiation factor 3 subunit L protein interacts with Flavivirus NS5 and may modulate yellow fever virus replication.. *Virology journal*. PMID: 23800076
5. Proteomic elucidation of the targets and primary functions of the picornavirus 2A protease.. *The Journal of biological chemistry*. PMID: 35367208

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 68.8 |
| 高置信度残基 (pLDDT>90) 占比 | 0.0% |
| 置信残基 (pLDDT 70-90) 占比 | 47.2% |
| 中等置信 (pLDDT 50-70) 占比 | 46.6% |
| 低置信 (pLDDT<50) 占比 | 6.2% |
| 有序区域 (pLDDT>70) 占比 | 47.2% |
| 可用 PDB 条目 | 3J8B, 3J8C, 6FEC, 6YBD, 6ZMW, 6ZON, 6ZP4, 6ZVJ, 7A09, 7QP6 |


**PAE (Predicted Aligned Error)**:
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/EIF3L/EIF3L-PAE.png]]

**评价**: AlphaFold 预测质量有限（pLDDT=68.8），有序残基占 47.2%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR019382, IPR000717, IPR011990; Pfam: PF10255 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| EIF3D | 0.999 | 0.995 | — |
| EIF3I | 0.999 | 0.980 | — |
| EIF3C | 0.999 | 0.989 | — |
| EIF3K | 0.999 | 0.998 | — |
| EIF3G | 0.999 | 0.980 | — |
| EIF3H | 0.999 | 0.995 | — |
| EIF3M | 0.999 | 0.991 | — |
| EIF3E | 0.999 | 0.998 | — |
| EIF3F | 0.999 | 0.994 | — |
| EIF3A | 0.999 | 0.992 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| EIF3K | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| XRN2 | psi-mi:"MI:0018"(two hybrid) | pubmed:15231747 |
| TBPH | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Dmel\CG10510 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Ranbp21 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Dmel\CG12256 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| COX4 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| DNM2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| Adsl | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| UQCR-C1 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=68.8 + PDB: 3J8B, 3J8C, 6FEC, 6YBD, 6ZMW,  | pLDDT=68.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm / Nucleoli; 额外: Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. EIF3L — Eukaryotic translation initiation factor 3 subunit L，非常新颖，仅有少数基础研究。
2. 蛋白大小564 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 22 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=68.8），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9Y262
- Protein Atlas: https://www.proteinatlas.org/ENSG00000100129-EIF3L/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=EIF3L
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9Y262
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleolus/EIF3L/EIF3L-PAE.png]]




