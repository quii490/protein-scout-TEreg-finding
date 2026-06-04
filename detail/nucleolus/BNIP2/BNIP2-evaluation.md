---
type: protein-evaluation
gene: "BNIP2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## BNIP2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | BNIP2 / NIP2 |
| 蛋白名称 | BCL2/adenovirus E1B 19 kDa protein-interacting protein 2 |
| 蛋白大小 | 314 aa / 36.0 kDa |
| UniProt ID | Q12982 |
| 评估日期 | 2026-06-03 |
| 数据采集时间 | 2026-06-03 03:41:20 |

**IF 图像**:
![](https://images.proteinatlas.org/26843/213_E10_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/26843/213_E10_2_blue_red_green.jpg)

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 5/10 | x4 | 20 | HPA: Cytosol; UniProt: Cytoplasm, Cyt... |
| 蛋白大小 | 10/10 | x1 | 10 | 314 aa / 36.0 kDa |
| 研究新颖性 | 4/10 | x5 | 20 | PubMed strict=61 篇 (61-80->4) |
| 三维结构 | 7/10 | x3 | 21 | AlphaFold v6 pLDDT=72.3 |
| 调控结构域 | 7/10 | x2 | 14 | InterPro: 3; Pfam: 2; IPR022181, IPR001251... |
| PPI 网络 | 10/10 | x3 | 30 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | -- | max +3 | 1.5 | 多库定位一致 (3源): +0.5; STRING + IntAct 双源验证: +0.5; 结构域 + AlphaFold 质量: +0.5 |
| **原始总分** | | | **116.5/180** | |
| **归一化总分 (/1.83)** | | | **63.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol; 额外: Nucleoli, Cytosol | Supported |
| UniProt | Cytoplasm, Cytoplasm, perinuclear region | Swiss-Prot/TrEMBL |

**IF 图像说明**: 原图已通过HPA检索获取，见上方嵌入图像。

**GO Cellular Component**:
- centriole (GO:0005814)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- intracellular membrane-bounded organelle (GO:0043231)
- nuclear envelope (GO:0005635)
- nucleolus (GO:0005730)
- perinuclear region of cytoplasm (GO:0048471)
- spindle pole centrosome (GO:0031616)

**结论**: 核定位证据一般，存在混合定位或不一致信号，需进一步实验验证。

#### 3.2 蛋白大小评估

**评价**: 314 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 61 |
| PubMed broad count | 75 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: NIP2 |

**关键文献**:
1. Estrogen neuroprotection: the involvement of the Bcl-2 binding protein BNIP2.. *Brain research. Brain research reviews*. PMID: 11744098
2. Astrocyte-derived exosomes carry microRNA-17-5p to protect neonatal rats from hypoxic-ischemic brain damage via inhibiting BNIP-2 expression.. *Neurotoxicology*. PMID: 33309839
3. miR-20a targets BNIP2 and contributes chemotherapeutic resistance in colorectal adenocarcinoma SW480 and SW620 cell lines.. *Acta biochimica et biophysica Sinica*. PMID: 21242194
4. ZSWIM8 is a myogenic protein that partly prevents C2C12 differentiation.. *Scientific reports*. PMID: 34686700
5. SIRT1 deficiency attenuates MPP+-induced apoptosis in dopaminergic cells.. *FEBS letters*. PMID: 21130087

**评价**: 研究较多，新颖性一般（PubMed 61-80篇）。新颖性评分 4/10。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 72.3 |
| 高置信度残基 (pLDDT>90) 占比 | 35.4% |
| 置信残基 (pLDDT 70-90) 占比 | 22.9% |
| 中等置信 (pLDDT 50-70) 占比 | 16.2% |
| 低置信 (pLDDT<50) 占比 | 25.5% |
| 有序区域 (pLDDT>70) 占比 | 58.3% |

**PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于AlphaFold pLDDT统计。**

**评价**: AlphaFold中等质量预测（pLDDT=72.3），存在部分低置信区域。三维结构评分 7/10。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR022181, IPR001251, IPR036865; Pfam: PF12496, PF13716 |

**染色质调控潜力分析**: 存在 5 个已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score > 0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| BCL2 | 0.982 | 0.618 | -- |
| CDC42 | 0.938 | 0.623 | -- |
| ARHGAP1 | 0.931 | 0.768 | -- |
| BNIP3 | 0.892 | 0.128 | -- |
| BNIP1 | 0.889 | 0.000 | -- |
| FRK | 0.798 | 0.796 | -- |
| PRUNE1 | 0.743 | 0.000 | -- |
| TTPA | 0.737 | 0.000 | -- |
| PRR5 | 0.681 | 0.050 | -- |
| CTNNA1 | 0.668 | 0.296 | -- |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| EWSR1 | two hybrid pooling approach | pubmed:16189514|imex:IM-16520|mint:MINT-5217968 |
| RCN3 | two hybrid pooling approach | pubmed:16189514|imex:IM-16520|mint:MINT-5217968 |
| CREB3 | two hybrid pooling approach | pubmed:16189514|imex:IM-16520|mint:MINT-5217968 |
| HSPA1A | two hybrid fragment pooling approach | pubmed:23414517|imex:IM-16425 |
| Aplp1 | cross-linking study | pubmed:17934213|imex:IM-19287 |
| wecA | two hybrid pooling approach | imex:IM-13779|pubmed:20711500 |
| ARHGAP1 | bioluminescence resonance energy transfe | pubmed:29997244|imex:IM-26441|doi:10.15252/msb.20178071 |
| PRUNE2 | cross-linking study | pubmed:30021884|imex:IM-26653|doi:10.1074/mcp.ra118.000924 |
| FYN | two hybrid fragment pooling approach | pubmed:31413325|imex:IM-26801 |
| FRK | two hybrid array | imex:IM-27438|doi:10.1038/s41467-019-11959-3|pubmed:31515488 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15

**评价**: 互作网络丰富：STRING 15 预测 + IntAct 15 实验互作。PPI 评分 10/10。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold v6 | pLDDT=72.3 | 单一来源 |
| 定位 | UniProt + HPA | Nucleoli / Cytoplasm, perinuclear region | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
**总分**: +1.5 / max +3

### 4. 总体评价

**归一化总分**: 63.7/100

**核心优势**:
1. 蛋白大小314 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。
2. 存在 5 个已知结构域，有明确的结构-功能切入点。

**风险/不确定性**:
1. 核定位信号较弱或存在矛盾（评分 5/10），需IF实验验证
2. 暂无PDB实验结构，结构证据完全依赖AlphaFold预测

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] 考虑通过AlphaFold预测 + MD模拟获取结构信息

### 5. 数据来源

- UniProt: https://www.uniprot.org/uniprotkb/Q12982
- Protein Atlas: https://www.proteinatlas.org/search/BNIP2
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=BNIP2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q12982
- STRING: https://string-db.org/network/9606.BNIP2
- Packet data timestamp: 2026-06-03 03:41:20
