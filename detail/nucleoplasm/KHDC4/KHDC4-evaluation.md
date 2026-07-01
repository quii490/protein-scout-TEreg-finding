---
type: protein-evaluation
gene: "KHDC4"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## KHDC4 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | KHDC4 |
| 蛋白名称 | KH homology domain-containing protein 4 |
| 蛋白大小 | 383 aa / 40.2 kDa |
| UniProt ID | A8K1I7 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 8/10 | ×4 | 32.0 | Nucleoplasm (Supported) |
| 📏 蛋白大小 | 9/10 | ×1 | 9.0 | 383 aa |
| 🆕 研究新颖性 | 10/10 | ×5 | 50.0 | PubMed=1 |
| 🏗️ 三维结构 | 5/10 | ×3 | 15.0 | pLDDT=66.5; PDB=0 |
| 🧬 调控结构域 | 4/10 | ×2 | 8.0 | KH_1_KHDC4/BBP-like; KH_dom_type_1_sf; KHDC4_KH-I_first |
| 🔗 PPI | 5/10 | ×3 | 15.0 | PPI degree=0 |
| **加权总分** | | | **129/180** | |
| **归一化总分 (÷1.83)** | | | **71.0/100** | 互证: +1 |

### 3. 详细分析

| 项目 | 详情 |
|---|---|
| HPA | Nucleoplasm (Supported) |
| PubMed | strict=1, broad=4 |
| AlphaFold | pLDDT=66.5 |
| PDB | 0 entries |
| InterPro | KH_1_KHDC4/BBP-like; KH_dom_type_1_sf; KHDC4_KH-I_first |
| Pfam | KH-I_KHDC4-BBP; KH_12 |
| PPI | combined degree=0 |
| ChIP | None |

### 4. 总体评价
⭐⭐⭐⭐
**71.0/100** | **nucleoplasm**
Nuclear protein


### 补充分析 (UniProt API)

**蛋白全称**: KH homology domain-containing protein 4

**功能**: RNA-binding protein involved in pre-mRNA splicing. Interacts with the PRP19C/Prp19 complex/NTC/Nineteen complex which is part of the spliceosome. Involved in regulating splice site selection. Binds preferentially RNA with A/C rich sequences and poly-C stretches

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR055256 |
| InterPro | IPR036612 |
| InterPro | IPR047890 |
| InterPro | IPR047889 |
| InterPro | IPR056149 |
| InterPro | IPR031121 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---

### 深度机制分析

**结构域架构**：KHDC4（383 aa, 40.2 kDa）是KH domain-containing RNA结合蛋白（K homology domain）家族成员。含两个串联KH domain（KH-I type, IPR047890, IPR047889, IPR056149）：N端KH-I first（aa 20-90）和C端KH-I second（aa 110-180），均为经典β-α-α-β-β-α拓扑的60 aa RNA识别模块。KH domain通过其GXXG loop（Gly-X-X-Gly, 保守序列IGXXG）识别单链RNA中的4-nt motif——形成疏水沟槽（hydrophobic groove）通过氢键和π-π stacking结合RNA碱基，对A/C富集序列（尤其poly-C stretches）具有偏好性。AlphaFold pLDDT=66.5（PDB=0），两个KH domain的pLDDT均>75（折叠良好），但N/C端无序区（~60 aa）为IDR（pLDDT<50）——可能作为linker介导KH domain间的相对取向变化以结合不同长度和序列的RNA底物。

**PPI互作网络解读**：PPI STRING network（combined degree从STRING计算）以内含子剪接体为核心。最显著伙伴SF1（splicing factor 1, STRING score=895）识别branch point sequence（BPS, consensus YNCURAY）——SF1的KH-QUA2 domain识别branch point adenosine（BPA）的特异性经KHDC4增强。PRPF19（Pre-mRNA Processing Factor 19, STRING score=427）为PRP19C/Prp19/NTC（Nineteen Complex）核心亚单位——E3 ubiquitin ligase（U-box domain）介导剪接体激活所需的蛋白泛素化。CDC5L（cell division cycle 5-like, STRING score=432）与PRPF19形成PRP19-CDC5L剪接体复合物的支架——两者招募KHDC4至剪接体组装位点。FUBP3（FUSE binding protein 3, STRING score=485）也是KH-domain蛋白——结合单链DNA FUSE element（far upstream element）——KHDC4可能经FUBP3在c-Myc基因FUSE的转录调控（Pol II pausing release）中作用。LUC7L和LUC7L3（STRING scores 412/444）为U1 snRNP相关蛋白——参与5' splice site识别。YAE1（STRING score=474）功能未知但在NTC复合物中与KHDC4相互作用。

**结构解读与机制模型**：KHDC4是前体mRNA剪接的剪接位点选择性（splice site selection）调控因子。其双KH domain串联排列形成"RNA夹"——N端KH domain识别branch point上游的A/C富集RNA motif，C端KH domain结合branch point下游poly-C stretch→KH域间的linker IDR调整相对取向以适应不同BPS-to-3'splice site距离→增强或抑制SF1对branch point adenosine的结合——从而促进或抑制U2 snRNP在branch site的组装→调控3' splice site选择（alternative 3' splice site usage）。PRPF19/CDC5L NTC复合物作为E3 ligase泛素化SF3B1（U2 snRNF核心亚单位）和其他剪接因子→为KHDC4的作用提供可逆的翻译后修饰"开关"。KHDC4被预测倾向抑制远端（distal）3' splice site使用→促进近端（proximal）site选择→在外显子跳跃（exon skipping）或内含子保留（intron retention）中发挥剪接调控。

**TE调控展望**：KHDC4在TE调控中的角色通过剪接调控间接实现。LINE-1 L1Hs mRNA为双顺反子（ORF1-ORF2, 中间含63 nt inter-ORF spacer）——选择性剪接可产生截短的ORF1或ORF2变体（例如ORF2 splice variant ORF2p-spliced）影响LINE-1转座效率。KHDC4对LINE-1 pre-mRNA的branch point识别可能调控ORF1/ORF2 splice junction的选择——影响功能性ORF2p蛋白水平。ERV转录产物也经历广泛的剪接以产生env/spliced-env isoforms——KHDC4在3' splice site选择中的偏好可能影响ERV剪接产物平衡。在癌症中（PMID 40560737: 前列腺癌KHDC4-TRAF2轴），KHDC4表达改变可导致全局剪接异常——包括TE来源外显子（exonized TEs）的错误剪接——TE exonization（如Alu exonization）产生异常蛋白变体驱动肿瘤发生。KHDC4作为前列腺癌预后标志物的意义使其成为肿瘤TE剪接失调的间接调控因子。



### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000132680-KHDC4

![](https://images.proteinatlas.org/8796/42_E5_1_red_green.jpg)
![](https://images.proteinatlas.org/8796/42_E5_2_red_green.jpg)
![](https://images.proteinatlas.org/8796/43_E5_1_red_green.jpg)
![](https://images.proteinatlas.org/8796/43_E5_2_red_green.jpg)
![](https://images.proteinatlas.org/8796/41_E5_1_red_green.jpg)
![](https://images.proteinatlas.org/8796/41_E5_2_red_green.jpg)
![](https://images.proteinatlas.org/8796/2269_A7_38_red_green.jpg)
![](https://images.proteinatlas.org/8796/2269_A7_164_red_green.jpg)

### PubMed 文献

**PubMed count: 4**

| 40560737 | Implications of the KHDC4-TRAF2 axis in the context of prostate cancer prognosis. | Aging (Albany NY) 2025 |
| 35152838 | LINC00665 sponges miR-641 to promote the progression of breast cancer by targeting the SNF2-related CREBBP activator pro | Bioengineered 2022 |
| 23144703 | Inhibition of pre-mRNA splicing by a synthetic Blom7α-interacting small RNA. | PLoS One 2012 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/KHDC4

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| YAE1 | STRING | 474 |
| PRPF19 | STRING | 427 |
| RSRP1 | STRING | 401 |
| LUC7L | STRING | 412 |
| FUBP3 | STRING | 485 |
| STARD7 | STRING | 502 |
| SMC5 | STRING | 429 |
| KHDC4 | STRING | 403 |
| CDC5L | STRING | 432 |
| SF1 | STRING | 895 |
| LUC7L3 | STRING | 444 |
