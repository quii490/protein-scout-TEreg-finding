---
type: protein-evaluation
gene: "KY"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## KY — REJECTED (研究热度过高 (PubMed strict=250，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | KY |
| 蛋白名称 | Kyphoscoliosis peptidase |
| 蛋白大小 | 661 aa / 75.2 kDa |
| UniProt ID | Q8NBH2 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm; UniProt: Cytoplasm, cytoskeleton; Cytoplasm, myofibril, sarcomere, Z  |
| 蛋白大小 | 10/10 | ×1 | 10 | 661 aa / 75.2 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=250 篇 (>100→REJECTED) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=79.7; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR052557, IPR056564, IPR038765, IPR002931; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 12 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **71.0/180** | |
| **归一化总分** | | | **39.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Approved |
| UniProt | Cytoplasm, cytoskeleton; Cytoplasm, myofibril, sarcomere, Z line | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytoskeleton (GO:0005856)
- Z disc (GO:0030018)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 250 |
| PubMed broad count | 66047 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. CDK8 inhibitor KY-065 rescues skeletal abnormalities in achondroplasia model mice.. *Biochimica et biophysica acta. Molecular basis of disease*. PMID: 39674288
2. Osteoblastgenic and Osteogenic Effects of KY-273 with CDK8/19 Inhibitory Activity in Bone Marrow Mesenchymal Stem Cells and Female Rats.. *Biological & pharmaceutical bulletin*. PMID: 38508765
3. Myofibrillar myopathy in the genomic context.. *Journal of applied genetics*. PMID: 30203143
4. Human gingiva transcriptome during wound healing.. *Journal of clinical periodontology*. PMID: 28005267
5. A herbal pair of Scutellaria barbata D. Don and Scleromitrion diffusum (Willd.) R.J. Wang induced ferroptosis in ovarian cancer A2780 cells via inducing heme catabolism and ferritinophagy.. *Journal of integrative medicine*. PMID: 39521705

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 79.7 |
| 高置信度残基 (pLDDT>90) 占比 | 60.1% |
| 置信残基 (pLDDT 70-90) 占比 | 19.1% |
| 中等置信 (pLDDT 50-70) 占比 | 2.4% |
| 低置信 (pLDDT<50) 占比 | 18.5% |
| 有序区域 (pLDDT>70) 占比 | 79.2% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 中等质量（pLDDT=79.7，有序区 79.2%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR052557, IPR056564, IPR038765, IPR002931; Pfam: PF23265, PF01841 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| MYBPC1 | 0.783 | 0.000 | — |
| FLNC | 0.727 | 0.066 | — |
| GPN2 | 0.552 | 0.091 | — |
| TTN | 0.497 | 0.000 | — |
| TRIM72 | 0.467 | 0.045 | — |
| BLMH | 0.454 | 0.000 | — |
| MSS51 | 0.449 | 0.079 | — |
| METAP1 | 0.429 | 0.101 | — |
| ANKRD29 | 0.412 | 0.094 | — |
| KLHL38 | 0.411 | 0.091 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 12，IntAct interactions: 0
- 调控相关比例: 0 / 12 = 0%

**评价**: STRING 12 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=79.7 + PDB: 无 | pLDDT=79.7, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm, cytoskeleton; Cytoplasm, myofibril, sar / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 12 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. KY — Kyphoscoliosis peptidase，研究基础较多，新颖性有限。
2. 蛋白大小661 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 250 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 250 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8NBH2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000174611-KY/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=KY
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8NBH2
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
