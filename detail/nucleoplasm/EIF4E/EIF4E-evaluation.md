---
type: protein-evaluation
gene: "EIF4E"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## EIF4E — REJECTED (研究热度过高 (PubMed strict=3266，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | EIF4E / EIF4EL1, EIF4F |
| 蛋白名称 | Eukaryotic translation initiation factor 4E |
| 蛋白大小 | 217 aa / 25.1 kDa |
| UniProt ID | P06730 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Cytosol, Cytoplasmic bodies; 额外: Nucleoplasm; UniProt: Cytoplasm, P-body; Cytoplasm; Cytoplasm, Stress granule; Nuc |
| 蛋白大小 | 10/10 | ×1 | 10 | 217 aa / 25.1 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=3266 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=90.9; PDB: 1IPB, 1IPC, 1WKW, 2GPQ, 2V8W, 2V8X, 2V8Y |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR023398, IPR001040, IPR019770; Pfam: PF01652 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **96.0/180** | |
| **归一化总分** | | | **53.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol, Cytoplasmic bodies; 额外: Nucleoplasm | Supported |
| UniProt | Cytoplasm, P-body; Cytoplasm; Cytoplasm, Stress granule; Nucleus; Nucleus speckle; Nucleus, nuclear ... | Swiss-Prot/TrEMBL |

**IF 图像获取**: 尝试获取IF原图中...

**GO Cellular Component**:
- chromatoid body (GO:0033391)
- cytoplasm (GO:0005737)
- cytoplasmic ribonucleoprotein granule (GO:0036464)
- cytoplasmic stress granule (GO:0010494)
- cytosol (GO:0005829)
- eukaryotic translation initiation factor 4F complex (GO:0016281)
- extracellular exosome (GO:0070062)
- glutamatergic synapse (GO:0098978)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 3266 |
| PubMed broad count | 4053 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: EIF4EL1, EIF4F |

**关键文献**:
1. Integrating fragment-based screening with targeted protein degradation and genetic rescue to explore eIF4E function.. *Nature communications*. PMID: 40016190
2. eIF4E-homologous protein (4EHP): a multifarious cap-binding protein.. *The FEBS journal*. PMID: 34758096
3. C8ORF88: A Novel eIF4E-Binding Protein.. *Genes*. PMID: 38003019
4. Mnks, eIF4E phosphorylation and cancer.. *Biochimica et biophysica acta*. PMID: 25450520
5. Progress in developing MNK inhibitors.. *European journal of medicinal chemistry*. PMID: 33892273

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 90.9 |
| 高置信度残基 (pLDDT>90) 占比 | 81.6% |
| 置信残基 (pLDDT 70-90) 占比 | 5.1% |
| 中等置信 (pLDDT 50-70) 占比 | 8.8% |
| 低置信 (pLDDT<50) 占比 | 4.6% |
| 有序区域 (pLDDT>70) 占比 | 86.7% |
| 可用 PDB 条目 | 1IPB, 1IPC, 1WKW, 2GPQ, 2V8W, 2V8X, 2V8Y, 2W97, 3AM7, 3TF2 |


**PAE**: PAE 图像未生成本地文件，结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（1IPB, 1IPC, 1WKW, 2GPQ, 2V8W, 2V8X, 2V8Y, 2W97, 3AM7, 3TF2）+ AlphaFold极高置信度预测（pLDDT=90.9），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR023398, IPR001040, IPR019770; Pfam: PF01652 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PABPC1 | 0.999 | 0.684 | — |
| EIF4A1 | 0.999 | 0.876 | — |
| EIF4EBP1 | 0.999 | 0.995 | — |
| EIF4A2 | 0.999 | 0.517 | — |
| EIF4EBP2 | 0.999 | 0.922 | — |
| EIF4G2 | 0.999 | 0.515 | — |
| EIF4B | 0.999 | 0.132 | — |
| EIF4EBP3 | 0.999 | 0.958 | — |
| EIF4G1 | 0.999 | 0.970 | — |
| EIF4ENIF1 | 0.999 | 0.966 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| EIF4G1 | psi-mi:"MI:0019"(coimmunoprecipitation) | pubmed:15361857 |
| eIF4E1 | psi-mi:"MI:0096"(pull down) | pubmed:14723848 |
| me31B | psi-mi:"MI:0019"(coimmunoprecipitation) | pubmed:14723848 |
| EIF4ENIF1 | psi-mi:"MI:0019"(coimmunoprecipitation) | pubmed:10856257 |
| smg | psi-mi:"MI:0096"(pull down) | pubmed:14685270|imex:IM-23094 |
| cup | psi-mi:"MI:0096"(pull down) | pubmed:14685270|imex:IM-23094 |
| EIF4EBP1 | psi-mi:"MI:0047"(far western blotting) | pubmed:7651417|mint:MINT-52204 |
| EMX2 | psi-mi:"MI:0019"(coimmunoprecipitation) | pubmed:15247416 |
| RanBPM | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| a10 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 4 / 15 = 27%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 27%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=90.9 + PDB: 1IPB, 1IPC, 1WKW, 2GPQ, 2V8W,  | pLDDT=90.9, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm, P-body; Cytoplasm; Cytoplasm, Stress gr / Cytosol, Cytoplasmic bodies; 额外: Nucleoplasm | 一致 |
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
1. EIF4E — Eukaryotic translation initiation factor 4E，研究基础较多，新颖性有限。
2. 蛋白大小217 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 3266 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 3266 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P06730
- Protein Atlas: https://www.proteinatlas.org/ENSG00000151247-EIF4E/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=EIF4E
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P06730
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
